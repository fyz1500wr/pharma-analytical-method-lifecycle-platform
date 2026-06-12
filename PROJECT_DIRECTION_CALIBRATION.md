# 藥品分析方法生命週期智慧平台 — 專案方向校準總結

## 1. 專案核心定位

本專案目標是建立一個 **Pharmaceutical Analytical Method Lifecycle Intelligence Platform**，中文定位為：**藥品分析方法生命週期智慧平台**。

本平台不是單純的分析方法報告產生器、確效 protocol 產生器、實驗室報告審閱工具或法規新聞追蹤器，而是支援完整分析方法生命週期的決策支援平台。

核心生命週期如下：

```text
產品分類
→ CQA / 分析目的對應
→ 分析項目與方法選擇
→ 分析方法開發策略
→ 方法條件優化
→ 確效 protocol 建立
→ 確效報告撰寫
→ 內部 / 外部實驗室文件審閱
→ 技術與法規缺失評估
→ 審閱結果回饋知識庫
```

平台應協助 CMC、RA、QA、PM、分析人員與文件審閱者，更快速、更有結構、且更可追溯地做出與藥品分析方法相關的判斷。

本系統必須定位為 **AI 輔助 + 專家審閱**，不可定位為自動核准系統，也不可取代 analytical SME、QA、RA 或 method owner 的最終判斷。

---

## 2. 專案核心目標

本平台應能支援以下功能：

1. 依產品類型、劑型、開發階段與分析目的進行分類。
2. 建議適合的分析項目與分析方法類型。
3. 以科學、風險導向與生命週期邏輯，協助分析方法開發與條件優化。
4. 協助產出分析方法開發報告草稿。
5. 協助產出分析方法確效 protocol 草稿。
6. 協助調整確效參數並產生 rationale。
7. 在有結構化數據時，協助產出分析方法確效報告草稿。
8. 協助審閱內部與外部實驗室文件，包括方法開發報告、確效 protocol、確效報告、方法轉移文件與技術提案。
9. 協助審閱者快速理解陌生或新興分析技術。
10. 協助找出技術、法規與文件缺失。
11. 產生 reviewer questions、vendor / lab follow-up questions 與 SME review flags。
12. 追蹤官方法規來源與經篩選的文獻 metadata，跟上法規與分析技術趨勢。
13. 將審閱結果回饋到專案知識庫，讓平台逐步累積組織記憶。

---

## 3. 架構原則

本專案初期應採用 **一個主 repo，多個模組**，而不是一開始就拆成多個互不相連的 repo。

本 repo 應作為分析方法生命週期規則、模板、法規 evidence pack、審閱邏輯與輸出文件的 single source of truth。

其他 CMC、法規、vendor management、eCTD 或 Notion 專案可以引用本 repo 的輸出，但不應複製或重新定義本 repo 內的核心分析方法規則。

建議主 repo 名稱：

```text
pharma-analytical-method-lifecycle-platform
```

---

## 4. 核心模組

### 模組 1：產品與分析目的分類模組

目的是在建議分析方法前，先釐清產品與分析目的。

輸入可包含：產品類型、分子類型、劑型、DS / DP / 原料 / IPC / 安定性樣品、臨床或商業化階段、release / stability / characterization / comparability / transfer 目的、目標法規區域、CQA、intended analytical purpose。

輸出包含：product profile、analytical intent、建議分析項目、風險區域、缺少資料清單。

### 模組 2：產品類型 / 分析方法矩陣

目的為將不同產品類型對應到可能需要的分析項目與方法類型。

此矩陣應支援 small molecule、peptide、recombinant protein、monoclonal antibody、ADC、oligonucleotide、vaccine、cell and gene therapy、complex formulation 等產品類型的逐步擴充。

此矩陣必須可擴充，不可只為單一產品、單一公司或單一分析方法硬寫邏輯。

### 模組 3：分析方法開發支援模組

目的為協助進行分析方法開發規劃與條件優化。

應支援：方法開發 rationale、critical method parameters、方法風險評估、screening experiment 建議、robustness study 建議、DoE / enhanced approach 建議、MODR 邏輯、system suitability 建議、troubleshooting 建議與方法開發報告架構。

此模組可以提出科學方向，但不得在沒有實驗數據時宣稱已找到最終最佳條件。

### 模組 4：確效 Protocol 產生模組

目的為依據方法目的、產品類型與法規期待，產生分析方法確效 protocol 草稿。

應支援 specificity / selectivity、accuracy、precision、repeatability、intermediate precision、linearity 或 calibration model、range / reportable range、LOD / LOQ、robustness、system suitability、sample / reagent stability、method transfer、partial validation、full validation、acceptance criteria rationale、experimental design、deviation handling rules。

所有輸出均為草稿，正式使用前必須經 analytical lead / QA / RA 審閱。

### 模組 5：確效報告產生模組

目的為在有結構化數據的前提下，協助產生確效報告草稿。

應支援 result summary tables、pass / fail assessment、statistical summaries、圖表、deviation summary、impact assessment、conclusion draft、limitation statement、human review requirement。

若沒有結構化數據，平台只能產生敘述性審閱或報告框架，不應產生確定性的確效結論。

### 模組 6：Technical Context-Aware Analytical Report Review Module

這是主平台底下的核心子模組，不是另一個獨立平台。

目的為協助 PM、審閱者、QA、RA 與 analytical lead 快速理解陌生、複雜或新興的分析技術報告。

此模組不應只是摘要報告，而應產生：

1. 技術原理卡：說明方法是什麼、測量什麼、訊號來源、可支持與不可支持的結論、限制與風險。
2. 方法適用性審閱：評估方法是否適合其宣稱的分析目的。
3. 法規與技術缺失評估：找出 rationale、數據、設計、確效與結論支持性的缺失。
4. Reviewer Question List：產生可用於詢問內部實驗室、外部 lab、CRO、CMO 或 vendor 的問題清單。
5. SME Review Flag：對新穎、複雜、資料不足或法規影響高的技術標記 SME review。
6. Evidence-Level Labeling：區分官方法規來源、內部規則表、文獻支援、vendor / lab 資料、AI 推論與人工審閱要求。

### 模組 7：法規 / 文獻 / 技術趨勢 Intelligence 模組

目的為讓平台能跟上官方法規與新興分析技術趨勢。

優先資料來源包含 ICH、FDA、EMA、TFDA、WHO / PMDA / EDQM metadata、PubMed / Europe PMC / Crossref metadata、內部歷史審閱結果與 curated internal knowledge base。

法規判斷應優先使用官方來源。文獻可協助理解技術原理，但不應直接被視為法規要求。Vendor 文件可作背景參考，但不能與官方 guidance 等同。

---

## 5. Claude、Codex、GitHub Actions 與 MCP 分工

### Claude

Claude 優先負責最終技術推理、法規解讀、分析方法開發 rationale、protocol 草稿、report 草稿、技術報告審閱、gap assessment、reviewer question generation 與 PM briefing note。

### Codex

Codex 優先負責 repo 維護、schema 實作、workflow 實作、GitHub Actions、tests、MCP server 開發、data pipeline、檔案架構更新與 PR 準備。

Codex 可在 schema 與 template 已清楚定義時產出初稿，但最終 CMC / RA / QA 判斷仍應透過 Claude 或專家環境審閱。

### GitHub Actions

GitHub Actions 用於定期刷新官方來源、抓取法規 metadata、產生 evidence pack、刷新文獻 metadata、schema validation、tests、artifact generation 與 dashboard data refresh。

### MCP

MCP 作為 AI 工具查詢 repo 內知識、法規來源、文獻 metadata 與內部規則的 access layer。

建議模式：

```text
GitHub Actions 抓取與整理來源
→ evidence packs 存入 repo
→ MCP 提供 curated evidence packs 與 rules
→ Claude / Codex 透過 MCP 查詢
→ 產生有來源標示的推理與文件
```

MCP 不應作為無限制即時搜尋工具。所有來源應經過分級、紀錄與 human review gate。

---

## 6. 來源與證據分級

所有輸出應區分證據類型。

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

建議信心等級：

```text
Confidence:
- High: 直接由官方 guidance 或已核准內部規則支持
- Medium: 由相關 guidance、常見實務或 curated literature 支持
- Low: 探索性建議，需要 SME review
```

平台不得把 AI 推論包裝成法規事實。

---

## 7. Human Review Gate

所有可能用於 CMC、QA、RA、實驗室、vendor 或法規用途的輸出，都必須保留人工審閱要求。

固定聲明：

```text
本文件由 AI 輔助產生，於 GxP、供應商溝通或法規用途使用前，必須由負責之 analytical lead、QA、RA 及 / 或 method owner 審閱確認。
```

平台可以協助決策，但不得自行核准 protocol、report、method、validation conclusion 或 regulatory strategy。

---

## 8. 新興分析技術處理原則

平台必須具備 Unknown / Emerging Analytical Technology Review Mode。

當遇到陌生或內部尚未 mapping 的分析技術時，不得強行給出確定結論。

技術狀態應分類為：

```text
Technology Status:
- Known and internally mapped
- Known but not internally mapped
- Emerging / insufficient internal knowledge
- Unclear terminology / requires clarification
```

若技術屬於 emerging 或 insufficiently mapped，平台應產生技術原理卡、查詢經篩選外部文獻或 metadata、說明該方法目前看起來測量什麼、說明該方法不能支持什麼、產生 SME 追問問題、標示 human-review-required，並避免宣稱該方法可直接作為 release、stability、comparability 或 regulatory filing 支持方法。

---

## 9. Feedback Loop 原則

平台應透過審閱結果持續強化。

每一次有價值的審閱結果，都應回饋到 common failure modes、reviewer question bank、method-specific checklist、product-type method matrix、validation gap rules、vendor / lab issue history、protocol template 與 report template。

範例：

```text
某 bioassay validation report 缺少 parallelism assessment
→ 記錄為 gap
→ 記錄 reviewer 追問問題
→ 記錄 lab 回覆
→ 未來同類 bioassay protocol 自動提醒 parallelism
→ 未來同類 validation report 審閱自動檢查 parallelism
```

---

## 10. 建議開發階段

### Phase 0：專案基礎建置

建立 README、PROJECT_INSTRUCTION、PROJECT_STATE_CONTINUATION、PROJECT_DIRECTION_CALIBRATION、architecture principles、source priority matrix、human review rule、evidence labeling rules、initial schemas 與 initial folder structure。

目標是在開始功能開發前，先防止架構漂移。

### Phase 1：Product → Method Matrix MVP

建立第一個實用 MVP。

輸入產品類型、劑型、DS / DP、開發階段、分析目的與法規區域。

輸出建議分析項目、建議方法類型、必要 / 視情況 / 選配分類、法規 rationale、缺少資訊與風險區域。

第一版可先聚焦 biologics / recombinant proteins / drug product release and stability，但架構必須保留未來擴充能力。

### Phase 2：Validation Protocol Generator

建立確效 protocol 產生能力，包括 validation characteristics、experimental design、acceptance criteria draft、sample and standard design、system suitability、deviation handling 與 report shell。

### Phase 3：Technical Context-Aware Report Review

建立分析報告審閱輔助能力。輸入內部或外部分析報告、method development report、validation protocol、validation report、method transfer report 或 vendor technical proposal；輸出技術原理卡、方法適用性評估、gap assessment、reviewer question list、SME review flag 與 evidence-level labeling。

### Phase 4：Regulatory and Literature Intelligence

加入 GitHub Actions regulatory source refresh、evidence pack generation、literature metadata refresh、MCP access layer 與 dashboard source update status。

### Phase 5：Closed-Loop Knowledge Management

加入 recurring gaps、question bank update、method checklist update、product-method matrix update、vendor / lab-specific issue tracking 與 protocol / report template improvement。

---

## 11. 本專案不應變成什麼

本專案不應變成：沒有結構化分析方法規則的一般 chatbot、單純 validation report template repository、沒有 method-level impact analysis 的法規新聞爬蟲、只服務單一 IFN 產品的知識庫、只有 Notion dashboard 但沒有 GitHub 版本控管規則的系統、宣稱能自動核准分析方法的工具、將文獻 / vendor 說法與官方 guidance 視為同等效力的系統、一堆彼此不連貫的 script、或 Claude / Codex / GitHub Actions / MCP 分工不清楚的混亂專案。

---

## 12. 未來方向校準問題

未來審閱 PR、新增模組或調整架構時，應用以下問題判斷是否偏離主軸：

1. 這個變更是否支援分析方法生命週期，而不只是單一 disconnected utility？
2. 是否保留未來擴充到 biologics / small molecule / peptide / mAb / ADC / oligonucleotide / cell therapy 等產品的能力？
3. 是否區分官方法規來源與 AI 推論？
4. 是否在需要時保留 human review gate？
5. 是否強化 product-method mapping、method development、validation、report review、regulatory intelligence 或 feedback learning？
6. 是否重複定義其他地方已存在的規則？
7. 是否能產生 source-traceable output？
8. 是否能幫助 PM、reviewer、analytical lead、QA 或 RA 做出更好的判斷？
9. 是否避免把產品特定假設硬寫進 general workflow？
10. 是否支援其他 CMC repo 或 Notion 引用，但不讓 Notion 成為核心知識庫？
11. 是否強化 Technical Context-Aware Report Review 能力或其知識庫？
12. 是否避免過度宣稱 AI 權威？

如果多數答案是否定的，該變更很可能偏離本專案核心方向。

---

## 13. 最終方向聲明

本專案方向是：建立一個具版本控管、可擴充、證據導向、AI 輔助的藥品分析方法生命週期平台，用於支援分析方法選擇、方法開發、確效規劃、確效報告、技術報告審閱、法規 intelligence 與知識回饋。

平台應協助使用者理解既有與新興分析技術，找出技術與法規缺失，產生高品質文件草稿，並支援 PM / CMC / QA / RA 的快速決策。

系統應依賴結構化規則、經篩選的法規 evidence、技術知識卡與 human review gates。系統不得取代專家判斷，也不得取代法規責任。

Technical Context-Aware Analytical Report Review Module 不是獨立平台，而是 Pharmaceutical Analytical Method Lifecycle Intelligence Platform 內的核心模組，並應被視為分析方法生命週期 feedback loop 的一部分。
