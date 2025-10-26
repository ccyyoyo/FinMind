# 多智能體設計

FinMind-Arena 集結五位核心 AI 分析師與一名協調者，模擬協作的投資決策委員會。

## 智能體陣容
| 智能體 | 專注領域 | 主要職責 | 建議模型 |
|--------|----------|----------|----------|
| 🧮 **基本面分析師** | 財務報表與公司體質 | 評估營收成長、EPS、槓桿與現金流趨勢，提供長期展望與估值觀點。 | `ProsusAI/finbert`、`BLOOM`、`Llama-3` |
| 📈 **技術面分析師** | 價格走勢與指標 | 追蹤均線、RSI、MACD 等訊號，判讀動能與短期趨勢。 | `TimeGPT`、`Informer`、`Temporal Fusion Transformer` |
| 🗞️ **新聞分析師** | 事件與頭條影響 | 摘要最新新聞、評估情緒，標記可能的利多或風險。 | `facebook/bart-large-cnn`、`ProsusAI/finbert` |
| 💬 **社群分析師** | 群眾情緒 | 探勘 Reddit、Twitter (X)、StockTwits 輿情，評估群眾共識。 | `cardiffnlp/twitter-roberta-base-sentiment`、`roberta-base-sentiment` |
| 🧠 **決策協調者** | 辯論主持與共識形成 | 編排多輪辯論、調和分歧觀點並發布最終建議。 | `GPT-4o-mini`、`Llama-3-70B`、ReAct / debate 框架 |

## 辯論流程
```
第 1 輪：各智能體提出觀點、佐證與信心分數。
第 2 輪：協調者挑戰假設，智能體回應或修正立場。
第 3 輪：進行投票並彙整為買進 / 持有 / 賣出結論。
```

## 協作框架
- **LangChain Multi-Agent**：處理工具調度、記憶與訊息傳遞。
- **Microsoft AutoGen**：提供辯論流程與角色化模板。
- **自訂邏輯**：根據領域需求調整信心水準權重與決策規則。

## 實作備註
- **模型取得**：TimeGPT 為 Nixtla 提供的商業 API。若需自部署選項，可考慮 `darts` 中的 TFT / Informer 實作，或使用 `Kats` 等套件建立傳統基準模型。
- **信心量化**：將各分析師的信心值正規化（例如 0–1 區間），方便協調者以一致邏輯整合意見。
- **防護機制**：設定檢驗規則（如資料新鮮度、波動度檢查），確保在條件不足時不會輸出不可靠的建議。
