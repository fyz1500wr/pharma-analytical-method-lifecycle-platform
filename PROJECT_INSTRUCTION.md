# PROJECT_INSTRUCTION

## 1. Project Mission

本 repo 是 **藥品分析方法生命週期智慧平台** 的主要執行與知識管理空間。

平台目標是支援藥品分析方法從產品分類、方法選擇、方法開發、條件優化、確效 protocol、確效報告、內外部實驗室文件審閱、法規與技術 intelligence，到審閱結果回饋知識庫的完整生命週期。

任何新增功能、文件、schema、workflow 或自動化，都必須對應 `PROJECT_DIRECTION_CALIBRATION.md` 內定義的專案方向。

---

## 2. Non-Negotiable Principles

1. 本平台是 AI-assisted / expert-reviewed，不是自動核准系統。
2. 官方法規來源、內部規則、文獻、vendor 資料與 AI 推論必須明確分層。
3. 所有 CMC、QA、RA、實驗室、供應商或法規用途輸出，都必須保留 human review gate。
4. 初期 MVP 可聚焦 biologics / recombinant proteins / DP release and stability，但架構不得寫死於單一產品或單一方法。
5. Notion 可作 dashboard 或任務追蹤，但 GitHub repo 才是規則、模板、source evidence 與版本控管的 single source of truth。
6. MCP 應作為 curated evidence / rules 的 access layer，不應作為無限制即時搜尋工具。
7. GitHub Actions 應優先用於官方來源刷新、evidence pack 生成、schema validation 與測試。

---

## 3. Tool Responsibilities

### Claude

優先負責：

- 法規與方法學推理
- 方法開發 rationale
- protocol / report 草稿
- 技術報告審閱
- gap assessment
- reviewer question generation
- PM briefing note
- final reasoning / direction calibration

### Codex

優先負責：

- repo 檔案與程式維護
- schema 實作
- workflow 實作
- GitHub Actions
- MCP server / connector 開發
- tests
- PR 整理
- data pipeline

### GitHub Actions

優先負責：

- regulatory source refresh
- literature metadata refresh
- evidence pack generation
- schema validation
- artifact generation
- dashboard data refresh

### MCP

優先負責：

- 將 repo 內 evidence packs、rules、knowledge base、templates 提供給 Claude / Codex / other clients 查詢。

---

## 4. Required Evidence Labels

所有正式輸出應盡可能標示：

```text
Evidence Level:
- Official regulatory source
- Internal rule table
- Curated scientific literature
- Vendor / laboratory-provided information
- Historical internal case
- AI-inferred suggestion
- Human review required
```

所有審閱或建議應盡可能標示：

```text
Confidence:
- High
- Medium
- Low
```

---

## 5. Human Review Statement

所有可能外部使用、供應商溝通、GxP 或法規用途輸出，必須包含以下聲明或等效文字：

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```

---

## 6. Repository Design Rules

1. 通用規則放在 `knowledge_base/`，不得藏在單一 workflow 或模板內。
2. 結構化資料格式放在 `schemas/`。
3. 可重複執行的操作邏輯放在 `workflows/`。
4. 文件草稿格式放在 `templates/`。
5. MCP 相關設計放在 `mcp/`。
6. 自動化放在 `.github/workflows/`。
7. Dashboard 規劃放在 `dashboard/`。
8. 程式碼放在 `src/`。
9. 測試放在 `tests/`。

---

## 7. Direction Calibration

任何 PR merge 前，應先檢查：

- 是否支援 analytical method lifecycle？
- 是否保留產品與方法擴充性？
- 是否區分 official source、internal rule、literature、vendor information、AI inference？
- 是否保留 human review gate？
- 是否避免把單一產品邏輯硬寫進通用 workflow？
- 是否能被其他 CMC repo 或 Notion dashboard 引用，而不造成規則重複？

若答案多數為否，該變更應暫緩或重新設計。
