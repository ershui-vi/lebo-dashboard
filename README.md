# 乐博经营数据看板

每日自动更新的乐博经营指标可视化看板，部署在 GitHub Pages 上。

## 看板内容

- **核心指标**: 新招生、净预收、税后课耗、活跃率、退费金额
- **趋势图表**: 近7天新招生/净预收/课耗/活跃率变化
- **全部明细**: 22项经营指标完整数据

数据来源: 一校教培系统 (`manage.shengtongedu.cn`) 每日取数。

## 文件结构

```
lebo-dashboard/
├── index.html              # 看板页面 (核心)
├── data.js                 # 数据文件 (看板加载)
├── data.json               # 数据备份 (JSON格式)
├── update_dashboard.py     # 本地更新脚本 (读取Excel→生成data.js→git push)
├── .github/
│   └── workflows/
│       └── update-dashboard.yml  # GitHub Actions 定时部署
└── README.md
```

## 部署步骤

### 1. 在 GitHub 创建仓库
- 登录 [github.com](https://github.com)，点击 New Repository
- 仓库名建议: `lebo-dashboard` (公开仓库免费)
- 不要勾选 README/.gitignore (我们已有文件)

### 2. 推送代码到 GitHub
```bash
cd C:\Users\张肖楠\WorkBuddy\2026-08-11-13-56-32\lebo-dashboard

# 初始化
git init
git add -A
git commit -m "初始化乐博经营数据看板"

# 关联远程仓库 (替换 YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/lebo-dashboard.git
git branch -M main
git push -u origin main
```

### 3. 开启 GitHub Pages
- 进入仓库 Settings → Pages
- Source 选择 **GitHub Actions**
- 等待 Actions 运行完成后，访问:
  `https://YOUR_USERNAME.github.io/lebo-dashboard/`

### 4. 每日自动更新 (二选一)

**方案A - 本地推送 (推荐)**:
在每日取数自动化任务后调用:
```bash
python update_dashboard.py
```
脚本会自动: 读取最新Excel → 更新 data.js → git commit → git push → GitHub Pages 自动更新

**方案B - GitHub Actions 自动**:
`.github/workflows/update-dashboard.yml` 已配置每天北京时间 07:00 自动部署。
(注: 此方案无法直接抓取一校教培数据，仅重新部署已有数据。需配合方案A推送数据。)

## 配置说明

`update_dashboard.py` 中的两个路径需要确认:
- `WORK_DIR`: 指标.xlsx 所在目录 (默认 `D:\龙虾工作空间`)
- `DASHBOARD_DIR`: 看板项目目录 (需改为你clone的仓库路径)

## 数据说明

| 指标 | 来源报表 |
|------|---------|
| 新招生(前端/后端) | 线条新招报表 |
| 总预收/退费/净预收 | 预收/退费报表 |
| 新招生预收/复购净预收 | 预收分类报表 |
| 税后课耗/常规课耗/单价/课次 | 课消单价报表 |
| 人均课次 | 人均课消次数 |
| 在籍学员/留存率 | 学员留存率 |
| 活跃学员/活跃率 | 学员活跃率 |
