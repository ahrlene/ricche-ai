"""
Generate the Institutional Research Whitepaper for Ricche Ltd.
Uses the same RicchePDF base class as the other three documents
for consistent branding and visual quality.
"""

from generate_all_pdfs import RicchePDF, NAVY, DARK, BODY_COLOR, ACCENT, NVIDIA_GREEN, LIGHT_BG, WHITE, GRAY, BORDER_COLOR
import os

OUT_DIR = os.path.dirname(__file__)


def generate_whitepaper():
    pdf = RicchePDF(
        'Institutional Research Whitepaper',
        'AI Infrastructure for the Future of Quantitative Market Research'
    )
    pdf.title_page()

    # ============================================================
    # PAGE 2: Executive Summary
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Executive Summary')
    pdf.body(
        'The quantitative finance industry is undergoing a fundamental transformation. '
        'The convergence of massive data availability, GPU-accelerated computing, and '
        'advances in machine learning has created an unprecedented opportunity to rethink '
        'how financial markets are studied, modelled, and understood.'
    )
    pdf.body(
        'Ricche Ltd is building the infrastructure for this new era. Our GPU-accelerated '
        'research platform combines institutional-grade data engineering, NVIDIA CUDA-powered '
        'machine learning environments, GPU-parallelised simulation engines, and rigorous '
        'validation frameworks into a single, cohesive system designed for one purpose: '
        'enabling the next generation of quantitative market research.'
    )
    pdf.body(
        'This whitepaper outlines our platform architecture, technology choices, research '
        'methodology, and the opportunity we see at the intersection of artificial intelligence '
        'and financial markets. It is intended for potential partners, technology collaborators, '
        'research institutions, and investors who share our vision.'
    )
    pdf.ln(2)
    pdf.quote_block(
        'We believe the firms that will define the next decade of quantitative finance are those '
        'building on AI-native, GPU-accelerated infrastructure from the ground up.'
    )
    pdf.ln(2)

    # Key stats
    pdf.stat_box('47x', 'GPU vs CPU Training', 15, pdf.get_y(), 42)
    pdf.stat_box('<2ms', 'Inference Latency', 62, pdf.get_y(), 42)
    pdf.stat_box('10B+', 'Data Points Ingested', 109, pdf.get_y(), 42)
    pdf.stat_box('30+', 'Global Exchanges', 156, pdf.get_y(), 38)
    pdf.ln(30)

    # ============================================================
    # PAGE 3: The Opportunity
    # ============================================================
    pdf.content_page()
    pdf.section_heading('The Opportunity')
    pdf.body(
        'Financial markets generate more data per day than most industries produce in a year. '
        'Tick-by-tick price movements across thousands of instruments, shifting order book '
        'dynamics, macroeconomic releases, corporate filings, satellite imagery, social '
        'sentiment -- the potential signal space is vast and growing exponentially.'
    )
    pdf.body(
        'Yet the infrastructure to process this data at scale remains locked behind the walls '
        'of a handful of the world\'s largest quantitative firms. Smaller teams, academic '
        'researchers, and new entrants face a stark choice: build expensive infrastructure '
        'from scratch, or work with inadequate tools that limit the scope and speed of '
        'their research.'
    )
    pdf.body(
        'Ricche exists to close this gap. We are building purpose-built, GPU-accelerated '
        'research infrastructure that brings institutional-grade computational power to '
        'quantitative market research -- infrastructure that compresses weeks of experimentation '
        'into hours and enables research at a scale that was previously impossible.'
    )
    pdf.ln(2)

    pdf.section_heading('Market Drivers')
    pdf.ensure_space(50)
    pdf.card_box(
        'Data Explosion',
        'Global financial data volumes are growing at 25-30% annually. Alternative data '
        'sources (satellite, NLP, sentiment) are adding entirely new dimensions to market '
        'analysis. Traditional tools cannot keep pace with this growth.',
        15, pdf.get_y(), 85, 45
    )
    pdf.card_box(
        'GPU Computing Revolution',
        'NVIDIA GPU computing has transformed machine learning from a niche technique '
        'to an industrial-scale capability. Training runs that took weeks on CPUs now '
        'complete in hours. This changes what is computationally feasible.',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(49)

    pdf.ensure_space(48)
    pdf.card_box(
        'AI Maturation in Finance',
        'Machine learning has moved beyond hype into proven production use across '
        'the financial sector. The question is no longer whether AI works in finance '
        '-- it is who has the best infrastructure to deploy it at scale.',
        15, pdf.get_y(), 85, 42
    )
    pdf.card_box(
        'Infrastructure Gap',
        'The gap between what leading firms can compute and what everyone else can '
        'access is widening. This creates a massive opportunity for purpose-built '
        'research infrastructure that levels the playing field.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(46)

    # ============================================================
    # PAGE 4: Platform Architecture
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Platform Architecture')
    pdf.body(
        'The Ricche platform is designed as a multi-layered research infrastructure where '
        'each layer is purpose-built for its specific workload and independently scalable. '
        'Data flows through five core layers, from raw market feeds to validated research outputs.'
    )
    pdf.ln(2)

    pdf.flow_arrow([
        'Market Data\nIngestion',
        'Data\nInfrastructure',
        'ML Research\nEnvironment',
        'Simulation\nFramework',
        'Validation\n& Governance'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Data Ingestion Layer')
    pdf.body(
        'Real-time and historical market data feeds from 30+ global exchanges including NYSE, '
        'CME, LSE, Eurex, HKEX, and SGX. The pipeline supports tick-level order book data, '
        'OHLCV pricing, corporate actions, economic indicators, and alternative data sources. '
        'Sub-second ingestion latency with exactly-once delivery guarantees, automatic gap '
        'detection, and continuous data quality scoring.'
    )

    pdf.sub_heading('GPU Compute Layer')
    pdf.body(
        'NVIDIA GPU clusters purpose-built for financial machine learning workloads. '
        'Distributed columnar storage (Apache Parquet, Arrow) for petabyte-scale datasets '
        'with intelligent tiering across NVMe, SSD, and object storage. Auto-scaling compute '
        'allocation with workload-aware priority scheduling ensures optimal GPU utilisation.'
    )

    pdf.sub_heading('Research & Experimentation Layer')
    pdf.body(
        'CUDA-accelerated PyTorch environments with comprehensive experiment tracking, model '
        'versioning, and automated hyperparameter optimisation. Every experiment is reproducible '
        'by design -- all code, data, parameters, and results are versioned and auditable. '
        'Support for deep learning, gradient boosting, transformers, and ensemble approaches.'
    )

    pdf.sub_heading('Simulation & Validation')
    pdf.body(
        'GPU-parallelised Monte Carlo and agent-based simulation engines that stress-test '
        'candidate models across 10,000+ market scenarios before progression. Formal validation '
        'stages with statistical significance testing, walk-forward analysis, and peer review '
        'ensure only genuinely robust models advance to controlled evaluation.'
    )

    # ============================================================
    # PAGE 5: NVIDIA GPU Infrastructure
    # ============================================================
    pdf.content_page()
    pdf.section_heading('NVIDIA Accelerated Computing Stack')
    pdf.body(
        'We chose to build Ricche on the full NVIDIA GPU ecosystem because there is no '
        'substitute for raw GPU performance when processing financial data at scale. The '
        'performance gains are not incremental -- they are transformational, enabling entirely '
        'new categories of research that were previously computationally infeasible.'
    )
    pdf.ln(2)

    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('DGX SuperPOD')
    pdf.nvidia_badge('NVIDIA GB200 NVL72')
    pdf.nvidia_badge('NVIDIA H200')
    pdf.nvidia_badge('BlueField-3 DPU')
    pdf.nvidia_badge('NVIDIA NIM')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('cuML')
    pdf.ln(12)

    pdf.ensure_space(58)
    pdf.nvidia_card_box(
        'NVIDIA CUDA -- The Foundation',
        'Every training run, every simulation, every feature computation is CUDA-accelerated. '
        'Multi-GPU distributed training with mixed-precision (FP16/BF16) delivers 47x speedups '
        'over CPU-only infrastructure. Researchers iterate on ideas in hours, not days. '
        'This is the engine that makes everything else possible.',
        15, pdf.get_y(), 85, 52
    )
    pdf.nvidia_card_box(
        'RAPIDS cuDF -- Data at GPU Speed',
        'Traditional CPU-bound data pipelines are the hidden bottleneck in most ML workflows. '
        'RAPIDS cuDF eliminates this entirely. Feature engineering on billion-row financial '
        'time-series runs 10-50x faster than pandas. End-to-end GPU processing means data '
        'never leaves the GPU between preparation and training.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    pdf.ensure_space(58)
    pdf.nvidia_card_box(
        'TensorRT -- Production Inference',
        'Research models are optimised for production through layer fusion, kernel auto-tuning, '
        'and INT8 quantisation. The result: sub-2ms inference latency for real-time signal '
        'generation. In markets where milliseconds matter, every microsecond of latency '
        'reduction translates directly to better research outcomes.',
        15, pdf.get_y(), 85, 52
    )
    pdf.nvidia_card_box(
        'NVIDIA NIM -- Production Deployment',
        'NVIDIA NIM microservices deliver optimised model inference with one-click deployment '
        'and dynamic scaling. Built-in model orchestration handles multi-model serving with '
        'intelligent batching and GPU memory management. Zero-downtime version transitions '
        'with automatic rollback and SLA monitoring.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    # Performance benchmarks
    pdf.ensure_space(30)
    pdf.green_stat_box('47x', 'GPU vs CPU Training', 15, pdf.get_y(), 42)
    pdf.green_stat_box('<2ms', 'Inference Latency', 62, pdf.get_y(), 42)
    pdf.green_stat_box('50x', 'Feature Eng. Speedup', 109, pdf.get_y(), 42)
    pdf.green_stat_box('10K+', 'Sim Scenarios/Run', 156, pdf.get_y(), 38)
    pdf.ln(28)

    # ============================================================
    # PAGE 6: Data Infrastructure & Coverage
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Data Infrastructure')
    pdf.body(
        'In quantitative research, data quality is not a nice-to-have -- it is the foundation '
        'on which every model, every simulation, and every research conclusion rests. Our '
        'multi-stage ingestion pipeline is engineered for institutional-grade reliability, '
        'because the best algorithms in the world are worthless when trained on dirty data.'
    )
    pdf.ln(2)

    pdf.flow_arrow([
        'Exchange\nFeeds',
        'Ingestion\nGateway',
        'Quality\nChecks',
        'Normalisation\n& Alignment',
        'Feature\nStore'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.section_heading('Global Market Coverage')
    pdf.bullet('Equities: Developed and emerging markets across 30+ exchanges worldwide')
    pdf.bullet('Futures & Commodities: Energy, metals, agriculture, financial futures (CME, ICE, LME)')
    pdf.bullet('Options: Full listed chains with Greeks, implied volatility surfaces, and skew data')
    pdf.bullet('Foreign Exchange: Spot, forwards, and crosses -- major and emerging market pairs')
    pdf.bullet('Fixed Income: Government bonds, investment-grade credit, interest rate instruments')
    pdf.bullet('Alternative Data: NLP-processed news, satellite imagery, social sentiment, web scraping')
    pdf.ln(4)

    pdf.section_heading('Data Quality Framework')
    pdf.body(
        'Every data point passes through a multi-stage quality assurance pipeline before entering '
        'the research environment. Automated checks for completeness, consistency, and statistical '
        'anomalies run continuously. Real-time data quality scoring with drift detection ensures '
        'researchers always work with clean, reliable datasets. Full data lineage tracking means '
        'any feature can be traced back to its raw source -- essential for reproducible research '
        'and regulatory compliance.'
    )

    pdf.ensure_space(44)
    pdf.card_box(
        'Real-Time Streaming',
        'Event-driven pipelines with sub-second latency and exactly-once delivery. '
        'Automatic reconnection and gap detection for exchange feeds. '
        'Sustained throughput of millions of events per second across all asset classes.',
        15, pdf.get_y(), 85, 38
    )
    pdf.card_box(
        'GPU-Accelerated Batch Processing',
        'Historical backfills and daily reconciliation powered by RAPIDS cuDF. '
        'Idempotent processing with complete audit trails and data versioning. '
        'Parallel GPU processing enables massive backfill operations in hours, not days.',
        110, pdf.get_y(), 85, 38
    )
    pdf.ln(42)

    # ============================================================
    # PAGE 7: Research Methodology
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Research Methodology')
    pdf.body(
        'Technology alone does not produce great research. Ricche enforces a disciplined, '
        'hypothesis-driven research methodology designed to eliminate the most dangerous traps '
        'in quantitative finance: overfitting, look-ahead bias, and narrative-driven analysis. '
        'Every experiment follows a structured workflow with built-in safeguards at each stage.'
    )
    pdf.ln(2)

    pdf.flow_arrow([
        'Research\nHypothesis',
        'Data\nPreparation',
        'Model\nDevelopment',
        'Simulation\nTesting',
        'Validation\n& Review'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('1. Hypothesis Registration')
    pdf.body(
        'Every project begins with a clearly defined hypothesis about market behaviour -- target '
        'instruments, timeframes, expected signal characteristics, and falsification criteria. '
        'Hypotheses are registered before any code is written. This prevents the most common '
        'failure mode in quantitative research: fitting a narrative to data after the fact.'
    )

    pdf.sub_heading('2. Data Preparation')
    pdf.body(
        'Datasets are extracted from the feature store with strict temporal discipline -- no '
        'look-ahead bias, ever. GPU-accelerated feature engineering using RAPIDS produces '
        'training-ready datasets 50x faster than traditional tools. Walk-forward splits ensure '
        'temporal consistency and real-world applicability.'
    )

    pdf.sub_heading('3. Model Development')
    pdf.body(
        'Models are developed in CUDA-accelerated PyTorch environments on NVIDIA GPU clusters. '
        'Experiment tracking captures every hyperparameter, metric, and artifact automatically. '
        'The 47x GPU speedup means researchers test more hypotheses per week than traditional '
        'setups allow in a month -- dramatically increasing the probability of discovery.'
    )

    pdf.sub_heading('4. Simulation Stress-Testing')
    pdf.body(
        'Candidate models face rigorous evaluation in GPU-parallelised simulation engines. '
        'Monte Carlo simulations test behaviour across 10,000+ scenarios including regime '
        'changes, liquidity crises, and tail events. Agent-based models capture market '
        'microstructure dynamics. Only models that survive this gauntlet progress.'
    )

    pdf.sub_heading('5. Validation & Peer Review')
    pdf.body(
        'Surviving models undergo out-of-sample validation, walk-forward testing, and formal '
        'peer review. Multiple hypothesis correction and bootstrap confidence intervals guard '
        'against overfitting. Approved models enter controlled paper-trading evaluation with '
        'strict position-size constraints and continuous performance monitoring.'
    )

    # ============================================================
    # PAGE 8: Operations & Monitoring
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Operations & Monitoring')
    pdf.body(
        'Running GPU-accelerated research infrastructure at scale demands complete, real-time '
        'visibility into every layer of the stack. The Ricche Control Room provides a unified '
        'operations dashboard that infrastructure operators and research leads use to monitor '
        'the entire platform -- from GPU memory allocation to data pipeline health to '
        'experiment progress.'
    )
    pdf.ln(2)

    pdf.stat_box('94.2%', 'GPU Utilisation', 15, pdf.get_y(), 42)
    pdf.stat_box('1,247', 'Active Experiments', 62, pdf.get_y(), 42)
    pdf.stat_box('3.2M', 'Events / sec', 109, pdf.get_y(), 42)
    pdf.stat_box('99.97%', 'Uptime (30d)', 156, pdf.get_y(), 38)
    pdf.ln(30)

    pdf.ensure_space(54)
    pdf.dark_card_box(
        'GPU Cluster Command',
        'Real-time utilisation heatmap across all GPU nodes. Per-GPU memory, temperature, '
        'power, and CUDA kernel metrics. Training job queue with priority scheduling. '
        'Thermal throttling detection and proactive failure prediction.',
        15, pdf.get_y(), 85, 48
    )
    pdf.dark_card_box(
        'Experiment Mission Control',
        'Live tracking of all active ML experiments with real-time loss curves and '
        'validation metrics. Per-experiment resource allocation and cost tracking. '
        'Automated early stopping recommendations and historical analytics.',
        110, pdf.get_y(), 85, 48
    )
    pdf.ln(52)

    pdf.ensure_space(48)
    pdf.dark_card_box(
        'Data Pipeline Operations',
        'Feed-by-feed ingestion status with per-exchange latency and throughput. '
        'Real-time data quality scoring with anomaly and drift detection. '
        'End-to-end pipeline lineage for full data traceability.',
        15, pdf.get_y(), 85, 42
    )
    pdf.dark_card_box(
        'Infrastructure Intelligence',
        'Kubernetes cluster orchestration with GPU scheduling queues. Predictive '
        'auto-scaling based on workload patterns. Storage tiering, network monitoring, '
        'and capacity forecasting with 30-day projections.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(46)

    # ============================================================
    # PAGE 9: Technology Stack
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Technology Stack')
    pdf.body(
        'Every tool in our stack was chosen for a specific reason -- performance, reliability, '
        'or researcher productivity. No resume-driven development, no hype cycles. Just the '
        'best technology for building world-class quantitative research infrastructure.'
    )
    pdf.ln(2)

    pdf.sub_heading('GPU & Accelerated Compute')
    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('DGX SuperPOD')
    pdf.nvidia_badge('NVIDIA GB200 NVL72')
    pdf.nvidia_badge('NVIDIA H200')
    pdf.nvidia_badge('BlueField-3 DPU')
    pdf.nvidia_badge('NVIDIA NIM')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('cuML')
    pdf.ln(10)

    pdf.sub_heading('Ultra-Low Latency Networking')
    pdf.tech_badge('InfiniBand NDR 400G')
    pdf.tech_badge('DPDK')
    pdf.tech_badge('RDMA')
    pdf.tech_badge('io_uring')
    pdf.tech_badge("Cap'n Proto")
    pdf.ln(10)

    pdf.sub_heading('Machine Learning & Research')
    pdf.tech_badge('PyTorch')
    pdf.tech_badge('JAX')
    pdf.tech_badge('Triton')
    pdf.tech_badge('FlashAttention-3')
    pdf.tech_badge('Liger Kernel')
    pdf.tech_badge('GaLore')
    pdf.tech_badge('Unsloth')
    pdf.tech_badge('vLLM')
    pdf.tech_badge('SGLang')
    pdf.tech_badge('Ray')
    pdf.tech_badge('W&B')
    pdf.ln(10)

    pdf.sub_heading('AI Agent Infrastructure')
    pdf.tech_badge('MCP')
    pdf.tech_badge('GraphRAG')
    pdf.ln(10)

    pdf.sub_heading('Data Engineering')
    pdf.tech_badge('Redpanda')
    pdf.tech_badge('Apache Iceberg')
    pdf.tech_badge('Apache DataFusion')
    pdf.tech_badge('Polars')
    pdf.tech_badge('DuckDB')
    pdf.tech_badge('ClickHouse')
    pdf.tech_badge('StarRocks')
    pdf.tech_badge('LanceDB')
    pdf.tech_badge('Turbopuffer')
    pdf.ln(10)

    pdf.sub_heading('Inference & Compute')
    pdf.tech_badge('Etched Sohu')
    pdf.tech_badge('Groq LPU')
    pdf.tech_badge('Modal')
    pdf.tech_badge('SkyPilot')
    pdf.ln(10)

    pdf.sub_heading('Infrastructure & Security')
    pdf.tech_badge('Kubernetes')
    pdf.tech_badge('Docker')
    pdf.tech_badge('Terraform')
    pdf.tech_badge('Temporal')
    pdf.tech_badge('Homomorphic Encryption')
    pdf.tech_badge('Confidential Computing')
    pdf.tech_badge('eBPF')
    pdf.tech_badge('OpenTelemetry')
    pdf.tech_badge('Prometheus')
    pdf.tech_badge('Grafana')
    pdf.ln(10)

    pdf.sub_heading('Core Languages')
    pdf.tech_badge('Python')
    pdf.tech_badge('Mojo')
    pdf.tech_badge('Rust')
    pdf.tech_badge('SQL')
    pdf.tech_badge('CUDA C++')
    pdf.ln(14)

    pdf.body(
        'Infrastructure-as-code (Terraform) ensures every deployment is reproducible. '
        'Temporal orchestrates complex ML workflows with built-in retry and observability. '
        'Ray distributes training and hyperparameter search across GPU clusters. Polars '
        'and DuckDB handle analytical queries at blazing speed. ClickHouse powers '
        'sub-second OLAP queries on financial time-series. Apache Iceberg provides '
        'the data lakehouse layer. Redpanda replaces Kafka with 10x lower latency '
        'and zero JVM overhead. Rust and Mojo power latency-critical paths.'
    )

    # ============================================================
    # PAGE 10: Vision, Partnerships & CTA
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Long-Term Vision')
    pdf.body(
        'Ricche is not a product -- it is a platform for discovery. Our long-term vision is '
        'to build the most capable research infrastructure for studying financial markets '
        'through artificial intelligence. We see a future where:'
    )
    pdf.ln(2)
    pdf.bullet('GPU-accelerated research infrastructure is as essential as market data itself')
    pdf.bullet('Machine learning approaches surpass traditional quantitative methods in every asset class')
    pdf.bullet('Real-time inference enables research insights that adapt to market conditions as they evolve')
    pdf.bullet('Simulation environments become the primary testing ground before any capital commitment')
    pdf.bullet('The best research comes from the best infrastructure, not the largest headcount')
    pdf.ln(6)

    pdf.section_heading('Partnership Opportunities')
    pdf.body(
        'Ricche sits at the intersection of three powerful forces: the explosion of available '
        'market data, the maturation of GPU-accelerated computing, and the proven superiority '
        'of machine learning approaches to financial modelling. We welcome collaboration with '
        'organisations that share this vision.'
    )
    pdf.ln(2)
    pdf.ensure_space(50)
    pdf.card_box(
        'Technology Partners',
        'GPU computing providers, cloud infrastructure companies, and hardware vendors '
        'looking to showcase accelerated computing in quantitative finance. We are an ideal '
        'reference platform for demonstrating real-world GPU performance gains.',
        15, pdf.get_y(), 85, 45
    )
    pdf.card_box(
        'Data Partners',
        'Market data vendors, alternative data providers, and exchange operators seeking '
        'a showcase platform for their data products. Our infrastructure demonstrates the '
        'full value of high-quality data when processed at GPU speed.',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(49)

    pdf.ensure_space(48)
    pdf.card_box(
        'Research Institutions',
        'Universities, research labs, and academic groups exploring AI applications in '
        'financial markets. We provide the computational infrastructure that enables '
        'research at a scale typically only available to top-tier quant firms.',
        15, pdf.get_y(), 85, 42
    )
    pdf.card_box(
        'Investors & Advisors',
        'Individuals and organisations interested in the convergence of artificial '
        'intelligence, quantitative finance, and high-performance computing. We are '
        'building for the decade ahead, not the quarter ahead.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(48)

    pdf.ensure_space(50)
    pdf.cta_block(
        'Let\'s Build the Future Together',
        'Whether you are a potential partner, investor, researcher, or technology collaborator, '
        'we would love to show you what GPU-accelerated market research looks like in practice.',
        'info@ricche.ai  |  ricche.ai'
    )

    out = os.path.join(OUT_DIR, 'ricche_institutional_whitepaper.pdf')
    pdf.output(out)
    print(f'Institutional Whitepaper: {out} ({os.path.getsize(out):,} bytes)')


if __name__ == '__main__':
    generate_whitepaper()
    print('\nWhitepaper generated successfully.')
