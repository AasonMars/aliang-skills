#!/usr/bin/env python3
"""根据正式记录生成面向日常使用的只读分类视图。"""
from pathlib import Path
import os
import subprocess
import sys
import tempfile

base = Path(__file__).resolve().parent.parent.parent
data = base / '系统文件/数据与索引'
workflow = base / '系统文件/自动化程序/scripts/workflow.py'
marker = '<!-- 由刷新能力视图.py生成；请勿手工编辑。 -->'
groups = {'待评估': [], '可使用': [], '观察中': []}


def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) < 3 or parts[0].strip():
        raise ValueError(f'记录缺少有效 frontmatter: {path}')
    result = {}
    for line in parts[1].splitlines():
        if ': ' in line:
            key, value = line.split(': ', 1)
            result[key.strip()] = value.strip().strip('"\'')
    return result


def label(value):
    return value.replace('|', '\\|').replace('\n', ' ')


def zh(value):
    return {'candidate': '候选', 'active': '已启用', 'reference': '参考', 'disabled': '已停用', 'quarantine': '隔离', 'healthy': '正常', 'unverified': '未验证', 'degraded': '性能下降', 'broken': '故障', 'missing': '缺失', 'not-installed': '未安装', 'project': '项目内', 'user': '用户级', 'global': '全局', 'external-service': '外部服务', 'retained': '已保留'}.get(value, value or '未知')


def grade_label(grade):
    labels = {'S': '核心资产', 'A': '已验证或强备用', 'B': '参考或待验证', 'C': '观察候选', 'D': '不保留'}
    return f'{grade}（{labels[grade]}）' if grade in labels else grade or '未评级'


def add(path, kind):
    record = frontmatter(path)
    rid = record.get('id')
    if not rid:
        raise ValueError(f'记录缺少 id: {path}')
    if kind == '能力':
        state = record.get('management_state', '')
        health = record.get('health_state', '')
        scope = record.get('deployment_scope', '')
        if state == 'retired':
            return
        if state == 'candidate':
            group = '待评估'
        elif state == 'active' and health == 'healthy' and scope not in ('', 'not-installed'):
            group = '可使用'
        else:
            group = '观察中'
        detail = f'管理：{zh(state)}；验证：{zh(health)}；部署：{zh(scope)}'
    else:
        state = record.get('status', '')
        grade = record.get('grade', '')
        if state in ('archived', 'rejected'):
            return
        group = '待评估' if state == 'candidate' else '观察中'
        detail = f'项目状态：{zh(state)}；等级：{grade_label(grade)}'
    display = rid
    relative = os.path.relpath(path, base / {'待评估':'待评估','可使用':'可使用','观察中':'观察中'}[group])
    groups[group].append(f'- [{label(display)}]({relative})（{kind}；{label(detail)}）')

for p in sorted((data / 'capabilities/records').glob('*.md')):
    add(p, '能力')
for p in sorted((data / 'projects/records').glob('*.md')):
    add(p, '项目')

for command in ('rebuild', 'validate'):
    subprocess.run([sys.executable, str(workflow), command, '--root', str(data)], check=True)

explanations = {
    '待评估': '发现了、已登记，但还需要评估或验证。',
    '可使用': '正式记录同时显示已启用、健康且有部署位置。实际使用前仍需确认当前环境和权限。',
    '观察中': '有待进一步判断的项目或能力，包括参考项目、未满足可使用条件的能力。',
}
folders = {'待评估':'待评估', '可使用':'可使用', '观察中':'观察中'}
for title, directory in folders.items():
    target = base / directory / 'README.md'
    if target.exists() and marker not in target.read_text(encoding='utf-8'):
        raise RuntimeError(f'为保护现有内容，未覆盖非生成文件: {target}')
    rows = '\n'.join(groups[title]) or '目前没有记录。'
    contents = f'{marker}\n# {title}\n\n{explanations[title]}\n\n{rows}\n\n状态来自正式记录；请让 AI 更新记录并刷新视图，不要直接修改本页。\n'
    with tempfile.NamedTemporaryFile('w', dir=target.parent, encoding='utf-8', delete=False) as tmp:
        tmp.write(contents)
        temp = tmp.name
    os.replace(temp, target)
print('能力分类视图已刷新。')
