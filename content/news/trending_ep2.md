---
title: "2026/05/14 本週 GitHub AI 趨勢"
date: 2026-05-14
draft: false
tags: ["GitHub趨勢", "AI週報", "AI Agent", "LLM應用", "開發者工具", "智能自動化"]
ShowToc: true
description: "本週 GitHub Trending 前 15 名中篩選出的 AI/LLM 相關專案整理"
---
{{< lang-toggle >}}

<div class="lang-zh">

本週從 GitHub Trending 前 15 名中，篩選出 **15 個** AI/LLM 相關專案：

---

## 1. [anthropics/financial-services](https://github.com/anthropics/financial-services)

> [→ GitHub 連結](https://github.com/anthropics/financial-services)

Anthropic 推出這套針對金融服務領域量身打造的 Claude 應用，無疑是本週最吸睛的亮點之一。這不僅僅是一個聊天機器人，它包含一系列預設好的 AI 代理、技能與資料連接器，專為投資銀行、股票研究、私募股權和財富管理等高門檻專業工作流設計。其亮點在於能自動生成投標簡報、執行市場研究、審閱財報、甚或協助 KYC 篩選，大幅提升效率。特別值得注意的是，專案強調所有輸出都需「人工簽核」，並嚴正聲明不構成投資建議，這精準回應了金融業對 AI 應用的嚴謹性和合規性要求。無論是作為 Claude Cowork 外掛或透過 Managed Agents API 部署，都展現了 LLM 在垂直領域的深化與實際落地潛力。

---

## 2. [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI)

> [→ GitHub 連結](https://github.com/Hmbown/DeepSeek-TUI)

DeepSeek-TUI 是一款引人注目的終端機程式碼 AI 助理，專為 DeepSeek V4 模型設計，旨在將 AI 編碼體驗無縫整合到開發者的日常工作流中。它不僅能在終端機內即時串流顯示 AI 的思考過程，更提供帶有審批機制的本地工作區編輯功能，大大提升編碼效率與透明度。其中，「自動模式」能智慧選擇模型與思維層級，有效平衡成本與性能。對於需要處理複雜開發任務的工程師而言，DeepSeek-TUI 的檔案操作、Shell 執行、Git 管理及多代理協同等完整工具套件，結合其對 1M-token 上下文的支援，使其成為一款提升生產力、同時注重安全性與成本效益的強大助手。

---

## 3. [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

> [→ GitHub 連結](https://github.com/bytedance/UI-TARS-desktop)

字節跳動開源的 UI-TARS-desktop 專案，為多模態 AI 代理領域帶來了令人振奮的進展。這套堆棧的核心是實現「人機互動」的自動化，特別是透過桌面應用程式提供原生的圖形使用者介面（GUI）代理，能夠操作本地與遠端電腦及瀏覽器。它解決了傳統 AI 難以直接理解和執行視覺化操作的痛點，讓 AI 代理能夠像人類一樣完成複雜的 GUI 任務，例如自動訂票、資料填寫等。結合了尖端多模態 LLM 和 MCP 工具整合，UI-TARS 展現了 AI 代理在超越文字、邁向真實世界互動的巨大潛力，對於推動通用 AI 助理的發展意義非凡。

---

## 4. [decolua/9router](https://github.com/decolua/9router)

> [→ GitHub 連結](https://github.com/decolua/9router)

9Router 是一個免費且高效的 AI 路由與代幣節省工具，其核心價值在於幫助開發者解決 AI 模型 API 的高昂成本與使用限制。它能將 Claude Code、Cursor、Copilot 等主流 AI 編碼工具，智能路由至超過 40 家供應商和 100 種模型，並具備智慧三層降級機制：優先使用訂閱、其次便宜模型、最後免費模型，確保編碼不間斷。更值得稱道的是其「RTK 代幣節省」功能，能自動壓縮工具輸出內容（如 Git diff），有效節省 20-40% 的輸入代幣。這對於重度依賴 AI 進行開發的工程師來說，無疑是個省錢又省心的利器，讓您再也不必擔心代幣用盡。

---

## 5. [yikart/AiToEarn](https://github.com/yikart/AiToEarn)

> [→ GitHub 連結](https://github.com/yikart/AiToEarn)

AiToEarn 是一個專為一人公司（OPC）、創作者、品牌與企業設計的 AI 內容行銷智能體平台。它徹底顛覆了傳統的內容創作與分發模式，透過 AI Agent 自動化「創作、發布、互動、變現」的完整流程。支援全球十多個主流社交與影音平台，讓內容能一鍵多平台發布，並利用 AI 智能回覆與評論挖掘來提升互動率。最核心的賣點在於其「內容賺錢」機制，提供 CPS、CPE、CPM 等多種結果導向的結算模式。AiToEarn 不僅是技術創新，更是商業模式的創新，預示著 AI 在未來內容經濟中扮演的關鍵角色，讓個人也能規模化地經營內容事業。

---

## 6. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> [→ GitHub 連結](https://github.com/rohitg00/agentmemory)

agentmemory 是一款開創性的 AI 編碼代理持久化記憶系統，旨在解決 AI 代理在跨會話情境下「健忘」的問題。它通過捕捉代理的每一次工具使用、壓縮成可搜索的記憶，並在下次會話開始時智能注入相關上下文，從根本上消除了重複解釋專案背景或決策的必要。基於 `iii-engine`，結合 BM25、向量和知識圖譜的混合搜索，以及獨特的四層記憶整合機制（工作、情節、語義、程序），其檢索準確度在業界基準測試中表現卓越。agentmemory 實質上為 AI 代理提供了一套可信賴的「大腦」，使其能夠累積經驗、持續學習，是構建更智能、更自主 AI 代理的關鍵基礎設施。

---

## 7. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> [→ GitHub 連結](https://github.com/addyosmani/agent-skills)

addyosmani/agent-skills 專案提供了一套「生產級」的 AI 編碼代理工程技能，將資深工程師在軟體開發生命週期中的最佳實踐、品質門檻和工作流程，轉化為 AI 代理可遵循的指令。這套技能旨在彌補 AI 代理傾向於採取「捷徑」的缺點，引導它們進行規範的設計、測試、程式碼審查與部署，提升輸出品質。專案的核心理念是讓 AI 代理成為有紀律的協作者，而非僅僅是程式碼生成器，諸如「規格驅動開發」、「測試驅動開發」等 Google 工程文化中的精髓也融入其中。它為構建可靠、可維護的 AI 輔助軟體提供了關鍵的流程框架。

---

## 8. [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research)

> [→ GitHub 連結](https://github.com/LearningCircuit/local-deep-research)

Local Deep Research 是一款強大的 AI 研究助理，專為深度、代理式研究而設計，能在單一 RTX 3090 等本地硬體上實現高達 95% 的 SimpleQA 準確度。其獨特之處在於，它不僅能利用多種 LLM 和十餘種搜索引擎（如 arXiv、PubMed、私人文件）進行廣泛搜索，還能將所有資訊綜合整理成帶有嚴謹引用的報告。更重要的是，它強調「完全本地化」與「加密」來保障用戶隱私與資料安全，讓研究查詢永不觸及外部伺服器。這對於需要處理敏感資料或重視隱私的學術機構、記者及企業而言，提供了一個極具吸引力的自主研究解決方案，讓資料掌控權回歸使用者。

---

## 9. [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader)

> [→ GitHub 連結](https://github.com/HKUDS/AI-Trader)

AI-Trader 是一個 100% 全自動化的「代理原生交易平台」，它提供了一個獨特的環境，讓 AI 代理能夠像人類交易員一樣，在股票、加密貨幣、外匯等多種主流市場中交流交易思路、精進技能。平台透過簡單的一行訊息即可實現任何 AI 代理的即時接入，使其能發布交易信號、參與社區討論、甚至一鍵跟單表現優異的代理。其核心價值在於聚合 AI 的集體智慧進行交易決策，同時允許與現有券商整合。AI-Trader 不僅為 AI 代理在金融領域的應用開闢了新天地，也為人類交易者提供了學習和獲利的新途徑，預示著金融自動化交易的未來。

---

## 10. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

> [→ GitHub 連結](https://github.com/Imbad0202/academic-research-skills)

Imbad0202/academic-research-skills 是一套專為學術研究設計的 Claude Code 技能套件，涵蓋從研究、寫作、審閱、修改到定稿的完整學術出版流程。其核心理念是讓 AI 成為研究者的「副駕駛」而非「主駕駛」，輔助處理繁瑣的文獻檢索、引用格式化、資料驗證、邏輯一致性檢查等工作。專案特別強調「人機協作」以避免 AI 的幻覺和偏見，並融入了如「魔鬼辯護者讓步閾值協議」等機制，促使 AI 進行更深入、更嚴謹的批判性思考。這套工具不僅提升了學術寫作效率，更致力於維護研究的誠信與品質，對於學術界利用 AI 進行高質量研究意義非凡。

---

## 11. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

> [→ GitHub 連結](https://github.com/ruvnet/ruflo)

Ruflo（原 Claude Flow）是一個領先的代理協同編排平台，專為 Claude Code 設計，能夠部署智慧型多代理群體，協調自主工作流，並構建對話式 AI 系統。它為 Claude Code 引入了協調式群體智慧、自學習記憶、聯邦式通訊和企業級安全功能，使 AI 代理不僅能運行，更能協同合作。Ruflo 透過先進的 SONA 神經模式與推理銀行，讓代理從每次任務中學習並優化。其獨特的「代理聯邦」功能，甚至能讓不同機器或組織的代理安全地跨信任邊界協作。這是一個將 AI 代理從單兵作戰推向大規模協作的里程碑式專案，具備強大的未來潛力。

---

## 12. [playcanvas/supersplat](https://github.com/playcanvas/supersplat)

> [→ GitHub 連結](https://github.com/playcanvas/supersplat)

SuperSplat Editor 是一款免費且開源的 3D Gaussian Splat 編輯器，以其基於 Web 技術的特性脫穎而出。這款工具讓使用者無需下載或安裝任何軟體，即可在瀏覽器中直接檢查、編輯、優化和發布 3D Gaussian Splat 檔案。儘管它本身並非 LLM 專案，但 3D Gaussian Splatting 作為新興的 3D 內容表示技術，與 AI 在生成式內容、虛擬實境和電腦視覺領域的結合日益緊密。SuperSplat 的出現，極大降低了這項先進技術的入門門檻，讓更多開發者和創作者能夠輕鬆探索和利用 AI 驅動的 3D 世界，為未來的元宇宙和沉浸式體驗奠定基礎。

---

## 13. [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)

> [→ GitHub 連結](https://github.com/VectifyAI/PageIndex)

PageIndex 是一款革命性的「無向量、基於推理」的 RAG（檢索增強生成）系統，專為處理長篇專業文件而生。它擺脫了傳統向量資料庫和分塊的限制，轉而透過建立文件的分層樹狀索引，並運用大型語言模型進行推理式檢索。這種方法模擬了人類專家如何透過目錄和結構來理解複雜文件，實現了更具上下文感知、可解釋且可追溯的檢索，大幅提升了在金融報告等領域的準確性（FinanceBench 上達 98.7%）。PageIndex 預示著 RAG 技術將從單純的語義相似性邁向更深層次的邏輯推理，對於需要高度精確和可信賴資訊檢索的企業應用意義重大。

---

## 14. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub 連結](https://github.com/mattpocock/skills)

Matt Pocock 提供的這套「為真實工程師打造的技能」是專為 AI 編碼代理設計的精髓，源自他日常的實際工程實踐。這套技能包旨在解決 AI 代理常見的開發痛點，如與用戶意圖的偏差、過於冗長的輸出以及程式碼品質問題。透過引入「拷問環節」來釐清需求，建立「共享語言」以提升溝通效率和程式碼一致性，並推廣「測試驅動開發」（TDD）來確保程式碼品質。這些技能強調將軟體工程的核心原則融入 AI 輔助開發流程，讓 AI 代理不再是盲目生成程式碼，而是成為一位具備紀律與設計思維的真正工程師，最終產出更可靠、可維護的應用。

---

## 15. [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)

> [→ GitHub 連結](https://github.com/datawhalechina/easy-vibe)

《Easy-Vibe》是 Datawhale China 推出的一門現代編程入門課程，以「Vibe Coding」為核心理念，即「會說話就能做應用」。這門課程旨在降低編程門檻，讓初學者、產品經理乃至創業者能透過直觀的對話式互動，將想法快速轉化為產品原型乃至完整的全棧應用。課程內容涵蓋了 AI 時代的開發工具、產品原型設計、AI 能力整合、前端/後端開發以及進階的 Claude Code 與 AI 代理工作流。其視覺化、互動式的教學方式，以及對 AI-native 開發模式的深入探討，使其成為引導新一代開發者掌握 AI 協作編程的理想學習資源。

</div>

<div class="lang-en">

This week, **15** AI/LLM-related projects have been selected from the top 15 on GitHub Trending:

---

## 1. [anthropics/financial-services](https://github.com/anthropics/financial-services)

> [→ GitHub Link](https://github.com/anthropics/financial-services)

Anthropic's launch of this tailored Claude application for the financial services sector is undoubtedly one of this week's most eye-catching highlights. More than just a chatbot, it comprises a suite of pre-configured AI agents, skills, and data connectors, specifically designed for high-barrier professional workflows such as investment banking, equity research, private equity, and wealth management. Its key features include automatically generating pitch decks, conducting market research, reviewing financial reports, and even assisting with KYC screening, significantly boosting efficiency. Notably, the project emphasizes that all outputs require "human sign-off" and explicitly states that it does not constitute investment advice. This precisely addresses the financial industry's stringent requirements for AI application rigor and compliance. Whether deployed as a Claude Cowork plugin or via the Managed Agents API, it demonstrates the deepening integration and practical application potential of LLMs in vertical sectors.

---

## 2. [Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI)

> [→ GitHub Link](https://github.com/Hmbown/DeepSeek-TUI)

DeepSeek-TUI is a remarkable terminal-based AI coding assistant, specifically designed for the DeepSeek V4 model, aiming to seamlessly integrate the AI coding experience into developers' daily workflows. It not only streams the AI's thought process live within the terminal but also provides local workspace editing features with an approval mechanism, significantly enhancing coding efficiency and transparency. Its "Auto Mode" intelligently selects models and reasoning levels, effectively balancing cost and performance. For engineers tackling complex development tasks, DeepSeek-TUI's comprehensive toolset—including file operations, Shell execution, Git management, and multi-agent collaboration—combined with its support for 1M-token contexts, makes it a powerful assistant for boosting productivity while prioritizing security and cost-effectiveness.

---

## 3. [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop)

> [→ GitHub Link](https://github.com/bytedance/UI-TARS-desktop)

ByteDance's open-source UI-TARS-desktop project brings exciting advancements to the field of multimodal AI agents. The core of this stack is to automate "human-computer interaction," specifically by providing native Graphical User Interface (GUI) agents through desktop applications capable of operating local and remote computers and browsers. It addresses the challenge of traditional AI struggling to directly understand and execute visual operations, enabling AI agents to complete complex GUI tasks like automated ticket booking and data entry, just like humans. By combining cutting-edge multimodal LLMs and MCP tool integration, UI-TARS demonstrates the immense potential of AI agents to move beyond text and interact with the real world, holding significant implications for advancing general AI assistants.

---

## 4. [decolua/9router](https://github.com/decolua/9router)

> [→ GitHub Link](https://github.com/decolua/9router)

9Router is a free and efficient AI routing and token-saving tool, whose core value lies in helping developers address the high costs and usage limitations of AI model APIs. It intelligently routes mainstream AI coding tools like Claude Code, Cursor, and Copilot to over 40 providers and 100 models, featuring a smart three-tier fallback mechanism: prioritizing subscriptions, then cheaper models, and finally free models, ensuring uninterrupted coding. Even more commendable is its "RTK token-saving" feature, which automatically compresses tool output content (e.g., Git diff), effectively saving 20-40% of input tokens. For engineers heavily reliant on AI for development, this is undoubtedly a cost-effective and worry-free tool, ensuring you no longer have to fear running out of tokens.

---

## 5. [yikart/AiToEarn](https://github.com/yikart/AiToEarn)

> [→ GitHub Link](https://github.com/yikart/AiToEarn)

AiToEarn is an AI content marketing agent platform designed for One-Person Companies (OPCs), creators, brands, and enterprises. It completely overturns traditional content creation and distribution models by automating the entire "creation, publication, interaction, and monetization" workflow through AI Agents. Supporting over a dozen mainstream social and video platforms globally, it enables one-click multi-platform content publishing and utilizes AI-powered intelligent replies and comment mining to boost interaction rates. The core selling point is its "content monetization" mechanism, offering various results-oriented settlement models like CPS, CPE, and CPM. AiToEarn is not just a technological innovation but also a business model innovation, heralding AI's pivotal role in the future content economy, allowing individuals to scale their content businesses.

---

## 6. [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)

> [→ GitHub Link](https://github.com/rohitg00/agentmemory)

agentmemory is a groundbreaking persistent memory system for AI coding agents, designed to solve the problem of AI agents being "forgetful" across sessions. It fundamentally eliminates the need to repeatedly explain project context or decisions by capturing every tool use by the agent, compressing it into searchable memories, and intelligently injecting relevant context at the start of the next session. Based on `iii-engine`, it combines hybrid search using BM25, vectors, and knowledge graphs, along with a unique four-layer memory integration mechanism (working, episodic, semantic, procedural), demonstrating excellent retrieval accuracy in industry benchmarks. agentmemory essentially provides AI agents with a reliable "brain," enabling them to accumulate experience and learn continuously, making it a critical infrastructure for building smarter, more autonomous AI agents.

---

## 7. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

> [→ GitHub Link](https://github.com/addyosmani/agent-skills)

The addyosmani/agent-skills project provides a set of "production-grade" engineering skills for AI coding agents, translating best practices, quality gates, and workflows from senior engineers in the software development lifecycle into instructions that AI agents can follow. This skillset aims to compensate for AI agents' tendency to take "shortcuts," guiding them towards disciplined design, testing, code review, and deployment, thereby improving output quality. The core philosophy of the project is to make AI agents disciplined collaborators rather than mere code generators, incorporating essences from Google's engineering culture, such as "specification-driven development" and "test-driven development." It provides a critical process framework for building reliable and maintainable AI-assisted software.

---

## 8. [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research)

> [→ GitHub Link](https://github.com/LearningCircuit/local-deep-research)

Local Deep Research is a powerful AI research assistant designed for in-depth, agentic research, capable of achieving up to 95% SimpleQA accuracy on local hardware such as a single RTX 3090. Its unique feature is that it not only leverages various LLMs and over a dozen search engines (like arXiv, PubMed, private documents) for extensive searches but also synthesizes all information into reports with rigorous citations. More importantly, it emphasizes "complete localization" and "encryption" to ensure user privacy and data security, meaning research queries never touch external servers. This offers a highly attractive autonomous research solution for academic institutions, journalists, and businesses that handle sensitive data or prioritize privacy, returning data control to the user.

---

## 9. [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader)

> [→ GitHub Link](https://github.com/HKUDS/AI-Trader)

AI-Trader is a 100% fully automated "agent-native trading platform" that provides a unique environment for AI agents to exchange trading ideas and refine their skills across multiple mainstream markets like stocks, cryptocurrencies, and forex, just like human traders. The platform allows instant integration of any AI agent with a simple one-line message, enabling them to publish trading signals, participate in community discussions, and even one-click copy the trades of top-performing agents. Its core value lies in aggregating the collective intelligence of AI for trading decisions while allowing integration with existing brokers. AI-Trader not only opens new avenues for AI agents in finance but also offers new learning and profit opportunities for human traders, foreshadowing the future of automated financial trading.

---

## 10. [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills)

> [→ GitHub Link](https://github.com/Imbad0202/academic-research-skills)

Imbad0202/academic-research-skills is a Claude Code skill suite specifically designed for academic research, covering the complete academic publication process from research, writing, review, and revision to finalization. Its core philosophy is to position AI as a researcher's "co-pilot" rather than the "main pilot," assisting with tedious tasks such as literature retrieval, citation formatting, data validation, and logical consistency checks. The project particularly emphasizes "human-AI collaboration" to mitigate AI hallucinations and biases, and incorporates mechanisms like the "devil's advocate concession threshold protocol" to encourage deeper, more rigorous critical thinking from the AI. This tool not only enhances academic writing efficiency but also strives to uphold research integrity and quality, holding significant implications for the academic community in utilizing AI for high-quality research.

---

## 11. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

> [→ GitHub Link](https://github.com/ruvnet/ruflo)

Ruflo (formerly Claude Flow) is a leading agent orchestration platform, designed for Claude Code, capable of deploying intelligent multi-agent groups, coordinating autonomous workflows, and building conversational AI systems. It introduces coordinated swarm intelligence, self-learning memory, federated communication, and enterprise-grade security features for Claude Code, enabling AI agents not just to operate, but to collaborate effectively. Through advanced SONA neural patterns and a reasoning bank, Ruflo allows agents to learn and optimize from every task. Its unique "agent federation" feature even enables agents from different machines or organizations to collaborate securely across trust boundaries. This is a landmark project transitioning AI agents from solo operation to large-scale collaboration, possessing powerful future potential.

---

## 12. [playcanvas/supersplat](https://github.com/playcanvas/supersplat)

> [→ GitHub Link](https://github.com/playcanvas/supersplat)

SuperSplat Editor is a free and open-source 3D Gaussian Splat editor, distinguished by its web-based technology. This tool allows users to directly inspect, edit, optimize, and publish 3D Gaussian Splat files in their browser without any software download or installation. Although not an LLM project itself, 3D Gaussian Splatting, as an emerging 3D content representation technology, is increasingly integrated with AI in generative content, virtual reality, and computer vision. The advent of SuperSplat significantly lowers the entry barrier for this advanced technology, enabling more developers and creators to easily explore and utilize AI-driven 3D worlds, laying the foundation for future metaverse and immersive experiences.

---

## 13. [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)

> [→ GitHub Link](https://github.com/VectifyAI/PageIndex)

PageIndex is a revolutionary "vector-free, inference-based" RAG (Retrieval Augmented Generation) system, specifically designed for handling long-form professional documents. It breaks free from the limitations of traditional vector databases and chunking by creating a hierarchical tree-like index of documents and employing large language models for inference-based retrieval. This method mimics how human experts understand complex documents through their structure and table of contents, achieving more context-aware, explainable, and traceable retrieval, significantly boosting accuracy in domains like financial reports (up to 98.7% on FinanceBench). PageIndex heralds RAG technology's shift from mere semantic similarity to deeper logical inference, holding significant implications for enterprise applications requiring highly precise and trustworthy information retrieval.

---

## 14. [mattpocock/skills](https://github.com/mattpocock/skills)

> [→ GitHub Link](https://github.com/mattpocock/skills)

The set of "skills for real engineers" provided by Matt Pocock is the essence designed for AI coding agents, derived from his daily practical engineering experience. This skill package aims to address common development pain points for AI agents, such as deviation from user intent, overly verbose outputs, and code quality issues. By introducing "interrogation sessions" to clarify requirements, establishing a "shared language" to improve communication efficiency and code consistency, and promoting "Test-Driven Development" (TDD) to ensure code quality, these skills emphasize integrating core software engineering principles into AI-assisted development workflows. This transforms AI agents from blindly generating code into true engineers with discipline and design thinking, ultimately producing more reliable and maintainable applications.

---

## 15. [datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)

> [→ GitHub Link](https://github.com/datawhalechina/easy-vibe)

"Easy-Vibe" is a modern programming introductory course launched by Datawhale China, centered on the philosophy of "Vibe Coding," which means "if you can talk, you can build applications." This course aims to lower the barrier to programming, enabling beginners, product managers, and even entrepreneurs to quickly transform ideas into product prototypes or even complete full-stack applications through intuitive conversational interaction. The curriculum covers development tools for the AI era, product prototype design, AI capability integration, front-end/back-end development, and advanced Claude Code and AI agent workflows. Its visual, interactive teaching approach and in-depth exploration of AI-native development patterns make it an ideal learning resource for guiding a new generation of developers to master AI-assisted programming.

</div>
