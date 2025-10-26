# 部署藍圖

本藍圖說明如何在前端、後端、模型服務與資料基礎設施上部署 FinMind-Arena。

## 環境職責
| 元件 | 責任歸屬 | 建議平台 |
|------|----------|----------|
| 前端 (Next.js UI) | 你的程式碼庫 | 部署至 Vercel 或 Zeabur，享有簡易 CI/CD。 |
| 後端 API (FastAPI / Node) | 你的程式碼庫 | 於 Render、Zeabur 或 AWS EC2 佈署。 |
| 多智能體協調器 | 你的程式碼庫 | 於後端服務內執行，搭配 LangChain 或 AutoGen。 |
| 外部模型 | 受管服務 | 透過 HuggingFace Inference API 或 OpenRouter 呼叫。 |
| 金融與社群 API | 受管服務 | 串接 Yahoo Finance、Finnhub、NewsAPI、Reddit、Twitter。 |
| 向量資料庫 | 混合模式 | 採用 Chroma、Weaviate 或 Supabase Vector，可自建或使用託管版本。 |

## 建議部署流程
1. **前端**：將 Next.js 專案推送至 GitHub，並連接 Vercel 自動建置。
2. **後端**：為 FastAPI/Node 應用建立 Dockerfile，部署至 Render/Zeabur，設定 API 金鑰環境變數。
3. **模型存取**：設定 HuggingFace Token 或 OpenRouter 憑證，透過遠端推論端點呼叫。
4. **資料庫**：建立 PostgreSQL + TimescaleDB 與向量儲存。Supabase 可同時提供關聯與向量功能。
5. **監控**：追蹤 API 使用率、協調器延遲與報告產出量。

## 環境管理
- **機密資訊**：使用平台提供的祕密管理（如 Render Secret Files、Zeabur Environment Variables、AWS Parameter Store），避免硬編碼憑證。
- **網路安全**：限制僅能對授權 API 網域發出請求，並以 TLS 保護資料庫連線。
- **測試關卡**：在 CI 中自動化整合測試（例如智能體辯論、資料擷取煙霧測試），確認無誤再發布至正式環境。
- **成本控管**：為第三方 API 與推論服務設定用量警示，及早發現異常支出。

## 部署架構概覽
```
使用者瀏覽器
   │
   ▼
Vercel / Zeabur (Next.js 前端)
   │
   ▼
Render / Zeabur / AWS EC2 (後端 API)
   ├── 多智能體協調器
   ├── 資料擷取工作器
   ├── RAG 記憶體管理
   └── 報告產生器
   │
   ├──► HuggingFace Hub (模型推論)
   ├──► 金融與新聞 API
   └──► Supabase / Chroma (資料儲存)
```

## 邁向正式環境的強化方向
- 為終端使用者加入身份驗證與使用額度管理。
- 建置前後端的 GitHub Actions 自動化部署流程。
- 導入記錄、追蹤與警示（如 OpenTelemetry、Sentry）。
- 當流量成長後，評估採用 Kubernetes 等容器編排方案。
- 透過功能旗標管理實驗性智能體或策略，降低對正式環境的風險。
