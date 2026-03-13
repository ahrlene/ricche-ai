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
    # PAGE 2: Executive Summary & The Opportunity
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
    pdf.ln(2)
    pdf.quote_block(
        'We believe the firms that will define the next decade of quantitative finance are those '
        'building on AI-native, GPU-accelerated infrastructure from the ground up.'
    )
    pdf.ln(2)

    # Key stats
    card_y = pdf.get_y()
    pdf.stat_box('47x', 'GPU vs CPU Training', 15, card_y, 42)
    pdf.stat_box('<2ms', 'Inference Latency', 62, card_y, 42)
    pdf.stat_box('141 GB', 'HBM3e per H200', 109, card_y, 42)
    pdf.stat_box('400G', 'InfiniBand NDR', 156, card_y, 38)
    pdf.set_y(card_y + 32)

    pdf.section_heading('The Opportunity')
    pdf.body(
        'Financial markets generate more data per day than most industries produce in a year -- '
        'tick-by-tick price movements, shifting order book dynamics, macroeconomic releases, '
        'satellite imagery, and social sentiment. Yet the infrastructure to process this data at '
        'scale remains locked behind the walls of the world\'s largest quantitative firms. Ricche '
        'exists to close this gap: purpose-built, GPU-accelerated research infrastructure that '
        'compresses weeks of experimentation into hours and enables research at a scale that was '
        'previously impossible.'
    )

    # ============================================================
    # PAGE 3: Platform Architecture
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
        'candidate models across thousands of market scenarios before progression. Formal validation '
        'stages with statistical significance testing, walk-forward analysis, and peer review '
        'ensure only genuinely robust models advance to controlled evaluation.'
    )

    # ============================================================
    # PAGE 4: NVIDIA GPU Infrastructure & Data
    # ============================================================
    pdf.content_page()
    pdf.section_heading('NVIDIA Accelerated Computing Stack')
    pdf.body(
        'We chose to build Ricche on the full NVIDIA GPU ecosystem because there is no '
        'substitute for raw GPU performance when processing financial data at scale. The '
        'performance gains are not incremental -- they are transformational.'
    )
    pdf.ln(2)

    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('DGX SuperPOD')
    pdf.nvidia_badge('NVIDIA GB200 NVL72')
    pdf.nvidia_badge('NVIDIA H200')
    pdf.nvidia_badge('BlueField-3 DPU')
    pdf.nvidia_badge('TensorRT-LLM')
    pdf.nvidia_badge('Triton Inference Server')
    pdf.nvidia_badge('Megatron-LM')
    pdf.nvidia_badge('NeMo Framework')
    pdf.nvidia_badge('NVIDIA NIM')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('cuML')
    pdf.ln(12)

    pdf.ensure_space(54)
    card_y = pdf.get_y()
    pdf.nvidia_card_box(
        'CUDA & RAPIDS -- GPU Foundation',
        'Every training run, simulation, and feature computation is CUDA-accelerated. '
        'Multi-GPU distributed training with mixed-precision (FP16/BF16) delivers dramatic '
        'speedups. RAPIDS cuDF eliminates CPU bottlenecks -- feature engineering on billion-row '
        'time-series runs 10-50x faster than pandas.',
        15, card_y, 85, 48
    )
    pdf.nvidia_card_box(
        'TensorRT & NIM -- Production Stack',
        'Research models optimised via layer fusion, kernel auto-tuning, and INT8 quantisation '
        'deliver sub-2ms inference latency. NIM microservices provide one-click deployment with '
        'dynamic scaling, intelligent batching, GPU memory management, and zero-downtime '
        'version transitions.',
        110, card_y, 85, 48
    )
    pdf.set_y(card_y + 52)

    # Performance benchmarks
    pdf.ensure_space(30)
    card_y = pdf.get_y()
    pdf.green_stat_box('141 GB', 'HBM3e per H200', 15, card_y, 42)
    pdf.green_stat_box('<2ms', 'Inference Latency', 62, card_y, 42)
    pdf.green_stat_box('400G', 'InfiniBand NDR', 109, card_y, 42)
    pdf.green_stat_box('5', 'Asset Classes', 156, card_y, 38)
    pdf.set_y(card_y + 32)

    pdf.section_heading('Data Infrastructure')
    pdf.body(
        'In quantitative research, data quality is the foundation on which every model and '
        'research conclusion rests. Our multi-stage ingestion pipeline covers equities, futures, '
        'options, FX, and fixed income across 30+ exchanges, with alternative data from NLP-processed '
        'news, satellite imagery, and social sentiment. Every data point passes through automated '
        'quality checks for completeness, consistency, and statistical anomalies. Full data lineage '
        'tracking ensures any feature can be traced to its raw source.'
    )

    # ============================================================
    # PAGE 5: Research Methodology & Operations
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Research Methodology')
    pdf.body(
        'Ricche enforces a disciplined, hypothesis-driven research methodology designed to '
        'eliminate the most dangerous traps in quantitative finance: overfitting, look-ahead '
        'bias, and narrative-driven analysis.'
    )
    pdf.ln(2)

    pdf.flow_arrow([
        'Hypothesis\nRegistration',
        'Data\nPreparation',
        'Model\nDevelopment',
        'Simulation\nTesting',
        'Validation\n& Review'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.body(
        'Every project begins with a registered hypothesis -- target instruments, timeframes, '
        'expected signal characteristics, and falsification criteria -- before any code is written. '
        'Datasets are extracted with strict temporal discipline (no look-ahead bias), with '
        'GPU-accelerated feature engineering producing training-ready datasets 50x faster than '
        'traditional tools.'
    )
    pdf.body(
        'Models are developed in CUDA-accelerated PyTorch environments with full experiment '
        'tracking. Candidate models face rigorous evaluation in GPU-parallelised simulation '
        'engines -- Monte Carlo simulations across thousands of scenarios including regime changes, '
        'liquidity crises, and tail events. Only models surviving out-of-sample validation, '
        'walk-forward testing, and formal peer review advance to controlled paper-trading evaluation.'
    )
    pdf.ln(4)

    pdf.section_heading('Operations & Monitoring')
    pdf.body(
        'The Ricche Control Room provides unified, real-time visibility into every layer of '
        'the stack -- from GPU memory allocation to data pipeline health to experiment progress.'
    )
    pdf.ln(2)

    card_y = pdf.get_y()
    pdf.stat_box('94.2%', 'GPU Utilisation', 15, card_y, 42)
    pdf.stat_box('128', 'Active Experiments', 62, card_y, 42)
    pdf.stat_box('2,540', 'Simulation Jobs', 109, card_y, 42)
    pdf.stat_box('99.97%', 'Uptime (30d)', 156, card_y, 38)
    pdf.set_y(card_y + 30)

    pdf.ensure_space(50)
    card_y = pdf.get_y()
    pdf.dark_card_box(
        'GPU Cluster Command',
        'Real-time utilisation heatmap across all GPU nodes. Per-GPU memory, temperature, '
        'power, and CUDA kernel metrics. Training job queue with priority scheduling and '
        'proactive failure prediction.',
        15, card_y, 85, 44
    )
    pdf.dark_card_box(
        'Data & Experiment Ops',
        'Live tracking of all ML experiments with real-time loss curves. Feed-by-feed '
        'ingestion status with per-exchange latency. Kubernetes orchestration with '
        'GPU scheduling, predictive auto-scaling, and capacity forecasting.',
        110, card_y, 85, 44
    )
    pdf.set_y(card_y + 48)

    # ============================================================
    # PAGE 6: Technology Stack
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Current Technology Stack')
    pdf.body(
        'Every tool in our stack was chosen for a specific reason -- performance, reliability, '
        'or researcher productivity.'
    )
    pdf.ln(2)

    pdf.sub_heading('GPU & Accelerated Compute')
    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('DGX SuperPOD')
    pdf.nvidia_badge('NVIDIA GB200 NVL72')
    pdf.nvidia_badge('NVIDIA H200')
    pdf.nvidia_badge('BlueField-3 DPU')
    pdf.nvidia_badge('TensorRT-LLM')
    pdf.nvidia_badge('Triton Inference Server')
    pdf.nvidia_badge('Megatron-LM')
    pdf.nvidia_badge('NeMo Framework')
    pdf.nvidia_badge('NVIDIA NIM')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('cuML')
    pdf.ln(10)

    pdf.sub_heading('ML & Research')
    pdf.tech_badge('PyTorch')
    pdf.tech_badge('JAX')
    pdf.tech_badge('Triton')
    pdf.tech_badge('FlashAttention-3')
    pdf.tech_badge('vLLM')
    pdf.tech_badge('Ray')
    pdf.tech_badge('W&B')
    pdf.ln(10)

    pdf.sub_heading('Data Engineering')
    pdf.tech_badge('KDB+/q')
    pdf.tech_badge('Arctic')
    pdf.tech_badge('Redpanda')
    pdf.tech_badge('Apache Iceberg')
    pdf.tech_badge('Apache DataFusion')
    pdf.tech_badge('Polars')
    pdf.tech_badge('DuckDB')
    pdf.tech_badge('ClickHouse')
    pdf.tech_badge('StarRocks')
    pdf.tech_badge('LanceDB')
    pdf.tech_badge('Turbopuffer')
    pdf.tech_badge("Cap'n Proto")
    pdf.ln(10)

    pdf.sub_heading('Networking & Low-Latency')
    pdf.tech_badge('InfiniBand NDR 400G')
    pdf.tech_badge('NVMe-oF')
    pdf.tech_badge('SPDK')
    pdf.tech_badge('DPDK')
    pdf.tech_badge('RDMA')
    pdf.tech_badge('io_uring')
    pdf.tech_badge('PTP (IEEE 1588)')
    pdf.ln(10)

    pdf.sub_heading('Trading & Execution')
    pdf.tech_badge('Aeron')
    pdf.tech_badge('FIX Protocol')
    pdf.tech_badge('LMAX Disruptor')
    pdf.tech_badge('ITCH / OUCH Protocol')
    pdf.tech_badge('Smart Order Routing')
    pdf.tech_badge('Backtesting Engine')
    pdf.ln(10)

    pdf.sub_heading('Platform & Security')
    pdf.tech_badge('Kubernetes')
    pdf.tech_badge('Docker')
    pdf.tech_badge('Argo CD')
    pdf.tech_badge('Cilium')
    pdf.tech_badge('Istio')
    pdf.tech_badge('HashiCorp Vault')
    pdf.tech_badge('Terraform')
    pdf.tech_badge('Temporal')
    pdf.tech_badge('AES-256')
    pdf.tech_badge('TLS 1.3')
    pdf.tech_badge('RBAC')
    pdf.tech_badge('eBPF')
    pdf.tech_badge('OpenTelemetry')
    pdf.tech_badge('Prometheus')
    pdf.tech_badge('Grafana')
    pdf.tech_badge('Audit Trail')
    pdf.ln(10)

    pdf.sub_heading('Core Languages')
    pdf.tech_badge('Python')
    pdf.tech_badge('Rust')
    pdf.tech_badge('SQL')
    pdf.tech_badge('CUDA C++')
    pdf.ln(10)

    pdf.body(
        'Terraform ensures reproducible deployments. Temporal orchestrates complex ML workflows. '
        'Ray distributes training across GPU clusters. Redpanda replaces Kafka with 10x lower '
        'latency. ClickHouse powers sub-second OLAP queries. Rust powers latency-critical paths.'
    )

    # ============================================================
    # PAGE 7: Vision, Partnerships & CTA
    # ============================================================
    pdf.content_page()
    pdf.section_heading('Long-Term Vision')
    pdf.body(
        'Ricche is not a product -- it is a platform for discovery. We see a future where '
        'GPU-accelerated research infrastructure is as essential as market data itself, where '
        'ML approaches surpass traditional quantitative methods in every asset class, and where '
        'the best research comes from the best infrastructure, not the largest headcount.'
    )
    pdf.ln(4)

    pdf.section_heading('Partnership Opportunities')
    pdf.body(
        'We welcome collaboration with organisations at the intersection of market data, '
        'GPU-accelerated computing, and machine learning.'
    )
    pdf.ln(2)
    pdf.ensure_space(50)
    card_y = pdf.get_y()
    pdf.card_box(
        'Technology Partners',
        'GPU computing providers, cloud infrastructure companies, and hardware vendors '
        'looking to showcase accelerated computing in quantitative finance.',
        15, card_y, 85, 38
    )
    pdf.card_box(
        'Data Partners',
        'Market data vendors, alternative data providers, and exchange operators seeking '
        'a showcase platform for their data products at GPU speed.',
        110, card_y, 85, 38
    )
    pdf.set_y(card_y + 42)

    pdf.ensure_space(44)
    card_y = pdf.get_y()
    pdf.card_box(
        'Research Institutions',
        'Universities and research labs exploring AI in financial markets. We provide '
        'computational infrastructure at a scale typically only available to top-tier quant firms.',
        15, card_y, 85, 38
    )
    pdf.card_box(
        'Investors & Advisors',
        'Individuals and organisations interested in the convergence of AI, quantitative '
        'finance, and high-performance computing. We are building for the decade ahead.',
        110, card_y, 85, 38
    )
    pdf.set_y(card_y + 44)

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
