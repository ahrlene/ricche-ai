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
    pdf.nvidia_badge('TensorRT-LLM')
    pdf.nvidia_badge('Triton Inference Server')
    pdf.nvidia_badge('Megatron-LM')
    pdf.nvidia_badge('NeMo Framework')
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
    pdf.nvidia_badge('TensorRT-LLM')
    pdf.nvidia_badge('Triton Inference Server')
    pdf.nvidia_badge('Megatron-LM')
    pdf.nvidia_badge('NeMo Framework')
    pdf.nvidia_badge('NVIDIA NIM')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('cuML')
    pdf.ln(10)

    pdf.sub_heading('Ultra-Low Latency Networking')
    pdf.tech_badge('InfiniBand NDR 400G')
    pdf.tech_badge('CXL Memory Pooling')
    pdf.tech_badge('NVMe-oF')
    pdf.tech_badge('SPDK')
    pdf.tech_badge('DPDK')
    pdf.tech_badge('RDMA')
    pdf.tech_badge('io_uring')
    pdf.tech_badge("Cap'n Proto")
    pdf.tech_badge('PTP (IEEE 1588)')
    pdf.ln(10)

    pdf.sub_heading('Quantitative Finance')
    pdf.tech_badge('KDB+/q')
    pdf.tech_badge('Arctic')
    pdf.tech_badge('Aeron')
    pdf.tech_badge('FIX Protocol')
    pdf.tech_badge('Xilinx Alveo FPGAs')
    pdf.tech_badge('LMAX Disruptor')
    pdf.tech_badge('ITCH / OUCH Protocol')
    pdf.tech_badge('Custom Matching Engine')
    pdf.tech_badge('Smart Order Routing')
    pdf.tech_badge('Queue Position Estimation')
    pdf.tech_badge('Exchange Co-location')
    pdf.ln(10)

    pdf.sub_heading('Adversarial Intelligence')
    pdf.tech_badge('Adversarial Order Flow Analysis')
    pdf.tech_badge('Full Market Digital Twin')
    pdf.tech_badge('Autonomous Strategy Discovery')
    pdf.tech_badge('RL Market Agents')
    pdf.tech_badge('Cross-Asset Regime Detection')
    pdf.tech_badge('Alpha Signal Library (10,000+)')
    pdf.tech_badge('Strategy Decay Monitoring')
    pdf.ln(10)

    pdf.sub_heading('Predatory Intelligence')
    pdf.tech_badge('Real-Time Strategy Fingerprinting')
    pdf.tech_badge('Competitor Model Decay Prediction')
    pdf.tech_badge('Alpha Extraction from Competitor Signals')
    pdf.tech_badge('Predictive Liquidation Detection')
    pdf.tech_badge('Stealth Execution Engine')
    pdf.tech_badge('Crisis Alpha Harvesting')
    pdf.tech_badge('Information Asymmetry Quantification')
    pdf.tech_badge('Counterparty Exposure Mapping')
    pdf.ln(10)

    pdf.sub_heading('Asymmetric Warfare')
    pdf.tech_badge('Shadow Portfolio Reconstruction')
    pdf.tech_badge('Strategy Replication Engine')
    pdf.tech_badge('Synthetic Information Derivation')
    pdf.tech_badge('Pre-Event Probability Engine')
    pdf.tech_badge('Correlated Failure Cascade Detection')
    pdf.tech_badge('Zero-Day Exchange Microstructure Exploits')
    pdf.tech_badge('Capital Structure Arbitrage Scanner')
    pdf.tech_badge('Market Impact Invisibility (< 0.01 bps)')
    pdf.tech_badge('Regulatory Horizon Scanning')
    pdf.tech_badge('Adversarial Self-Attack Simulation')
    pdf.ln(10)

    pdf.sub_heading('Self-Evolving Alpha System')
    pdf.tech_badge('Self-Evolving Alpha Engine')
    pdf.tech_badge('Autonomous Deploy & Replace')
    pdf.tech_badge('Regime-Adaptive Execution')
    pdf.tech_badge('Sharpe > 3 Target Architecture')
    pdf.ln(10)

    pdf.sub_heading('Proprietary Data Moats')
    pdf.tech_badge('Exclusive Alternative Data Feeds')
    pdf.tech_badge('Proprietary Sentiment Pipelines')
    pdf.tech_badge('Dark Pool Flow Reconstruction')
    pdf.tech_badge('Cross-Market Correlation Maps')
    pdf.tech_badge('Satellite & IoT Data Ingestion')
    pdf.tech_badge('Supply Chain Telemetry')
    pdf.ln(10)

    pdf.sub_heading('Speed-of-Light Infrastructure')
    pdf.tech_badge('Private Microwave Networks')
    pdf.tech_badge('Millimeter Wave (mmWave)')
    pdf.tech_badge('Hollow-Core Fiber')
    pdf.tech_badge('Point-to-Point Laser Links')
    pdf.tech_badge('Custom NIC Firmware')
    pdf.tech_badge('Nanosecond Timestamping')
    pdf.ln(10)

    pdf.sub_heading('Kernel-Level Optimisation')
    pdf.tech_badge('AF_XDP')
    pdf.tech_badge('Busy-Polling')
    pdf.tech_badge('isolcpus / nohz_full')
    pdf.tech_badge('1GB HugePages')
    pdf.tech_badge('Tick-to-Trade < 1us')
    pdf.ln(10)

    pdf.sub_heading('Custom Operating System')
    pdf.tech_badge('Custom Linux Kernel (PREEMPT_RT)')
    pdf.tech_badge('Unikernel')
    pdf.tech_badge('Custom Kernel Modules')
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

    pdf.sub_heading('Platform Engineering')
    pdf.tech_badge('Kubernetes')
    pdf.tech_badge('Docker')
    pdf.tech_badge('Argo CD')
    pdf.tech_badge('Cilium')
    pdf.tech_badge('Istio')
    pdf.tech_badge('Crossplane')
    pdf.tech_badge('Backstage')
    pdf.tech_badge('HashiCorp Vault')
    pdf.tech_badge('Terraform')
    pdf.tech_badge('Temporal')
    pdf.ln(10)

    pdf.sub_heading('Quantum & Next-Gen Computing')
    pdf.tech_badge('Qiskit')
    pdf.tech_badge('PennyLane')
    pdf.tech_badge('Post-Quantum Cryptography')
    pdf.tech_badge('Photonic Computing')
    pdf.tech_badge('Neuromorphic Computing')
    pdf.ln(10)

    pdf.sub_heading('Custom Silicon')
    pdf.tech_badge('Custom ASIC Tape-out')
    pdf.tech_badge('Chisel / SpinalHDL')
    pdf.tech_badge('Cadence / Synopsys EDA')
    pdf.ln(10)

    pdf.sub_heading('Sovereign Compute Infrastructure')
    pdf.tech_badge('Private Satellite Data Downlink')
    pdf.tech_badge('Submarine Cable Tap Rights')
    pdf.tech_badge('Private Spectrum Licensing')
    pdf.tech_badge('Sovereign AI Compute Cluster')
    pdf.tech_badge('Orbital Edge Compute')
    pdf.tech_badge('Geothermal-Powered Compute')
    pdf.tech_badge('Private Autonomous Drone Fleet')
    pdf.tech_badge('Proprietary Foundation Model')
    pdf.ln(10)

    pdf.sub_heading('Infrastructure Dominance')
    pdf.tech_badge('Private Global Backbone Network')
    pdf.tech_badge('Custom SmartNIC (P4-Programmable)')
    pdf.tech_badge('In-Network Compute (Switch-Level)')
    pdf.tech_badge('Liquid / Immersion Cooling')
    pdf.tech_badge('Edge Inference at Exchange PoPs')
    pdf.tech_badge('Multi-Region Active-Active Architecture')
    pdf.tech_badge('Automated Regulatory Compliance Engine')
    pdf.tech_badge('Self-Healing Infrastructure')
    pdf.ln(10)

    pdf.sub_heading('Talent & Intelligence Warfare')
    pdf.tech_badge('Automated Talent Acquisition Engine')
    pdf.tech_badge('Proprietary Knowledge Graph')
    pdf.tech_badge('Natural Language Strategy Interface')
    pdf.tech_badge('Real-Time Earnings Call NLP')
    pdf.tech_badge('Digital Twin of Global Economy')
    pdf.tech_badge('Autonomous Research Lab')
    pdf.tech_badge('Enterprise-Grade Audit Trail')
    pdf.tech_badge('Multi-Modal Data Fusion Engine')
    pdf.ln(10)

    pdf.sub_heading('Orbital & Deep-Space Alpha')
    pdf.tech_badge('LEO Satellite Constellation (Proprietary)')
    pdf.tech_badge('Space-Based RF Signal Intelligence')
    pdf.tech_badge('Rocket-Deployed Edge Nodes')
    pdf.tech_badge('Cislunar Communication Relay')
    pdf.tech_badge('Radiation-Hardened Trading Core')
    pdf.tech_badge('Hypersonic Data Couriers')
    pdf.tech_badge('Planetary-Scale Sensor Mesh')
    pdf.tech_badge('Launch-on-Demand Infrastructure')
    pdf.tech_badge('Space Weather Alpha')
    pdf.ln(10)

    pdf.sub_heading('Autonomous Physical Intelligence')
    pdf.tech_badge('Autonomous Trading Floor (Zero Humans)')
    pdf.tech_badge('Neural Market Architecture')
    pdf.tech_badge('Real-Time Energy Market Arbitrage')
    pdf.tech_badge('Predictive Supply Chain Robotics')
    pdf.tech_badge('Battery & Commodity Forward Curve AI')
    pdf.tech_badge('Manufacturing Throughput Alpha')
    pdf.tech_badge('Embodied AI Market Agents')
    pdf.tech_badge('Autonomous Fleet Telemetry Alpha')
    pdf.tech_badge('Self-Replicating Infrastructure')
    pdf.ln(10)

    pdf.sub_heading('Closed-Ecosystem Supremacy')
    pdf.tech_badge('Custom Trading SoC (System-on-Chip)')
    pdf.tech_badge('On-Device Federated Alpha')
    pdf.tech_badge('Zero-Knowledge Portfolio Proofs')
    pdf.tech_badge('Unified Trading OS')
    pdf.tech_badge('Sub-Pixel Market Visualisation Engine')
    pdf.tech_badge('Biometric Operator Authentication')
    pdf.tech_badge('Hardware Security Enclave (Trading)')
    pdf.tech_badge('Silent Intelligence Network')
    pdf.tech_badge('End-to-End Encrypted Execution Pipeline')
    pdf.ln(10)

    pdf.sub_heading('GPU-Native Financial Supercomputing')
    pdf.tech_badge('Multi-Die GPU Chiplet Trading Engine')
    pdf.tech_badge('GPU-Direct RDMA to Exchange')
    pdf.tech_badge('Tensor Core Risk Engine')
    pdf.tech_badge('CUDA Graph Execution Pipelines')
    pdf.nvidia_badge('Grace Hopper Superchip Cluster')
    pdf.nvidia_badge('DGX Cloud Private Instance')
    pdf.nvidia_badge('Optical Interconnect (NVLink C2C)')
    pdf.tech_badge('GPU-Accelerated Monte Carlo (10B paths/sec)')
    pdf.nvidia_badge('cuQuantum Financial Simulation')
    pdf.ln(10)

    pdf.sub_heading('Omniscient Data Supremacy')
    pdf.tech_badge('Global Information Arbitrage Engine')
    pdf.tech_badge('Exascale Feature Store')
    pdf.tech_badge('Transformer-Native Trading Architecture')
    pdf.tech_badge('Real-Time Knowledge Graph (Trillion Edges)')
    pdf.tech_badge('TPU-Optimised Alpha Discovery')
    pdf.tech_badge('Synthetic Data Generation at Scale')
    pdf.tech_badge('Intent-Based Market Search')
    pdf.tech_badge('Continuous Learning Production Models')
    pdf.tech_badge('Petabyte-Scale Backtesting Engine')
    pdf.ln(10)

    pdf.sub_heading('Social Graph Weaponisation')
    pdf.tech_badge('Collective Sentiment Topology')
    pdf.tech_badge('Viral Alpha Propagation Model')
    pdf.tech_badge('Social Influence Weighted Order Flow')
    pdf.tech_badge('Deepfake Detection for Market Manipulation')
    pdf.tech_badge('Attention Economy Alpha')
    pdf.tech_badge('Behavioural Contagion Predictor')
    pdf.tech_badge('Real-Time Narrative Extraction Engine')
    pdf.tech_badge('Metaverse Economic Intelligence')
    pdf.tech_badge('Human Behaviour Foundation Model')
    pdf.ln(10)

    pdf.sub_heading('Custom Silicon Dominance')
    pdf.tech_badge('Custom Network ASIC (Trading-Optimised)')
    pdf.tech_badge('Photonic Switching Fabric')
    pdf.tech_badge('SerDes IP at 224G PAM4')
    pdf.tech_badge('Custom PCIe Gen 6 Controller')
    pdf.tech_badge('On-Chip Hardware Timestamping (Sub-Nanosecond)')
    pdf.tech_badge('Silicon Photonics Co-Packaged Optics')
    pdf.tech_badge('Custom Memory Controller (HBM4 Interface)')
    pdf.tech_badge('ASIC-Accelerated Compression Engine')
    pdf.tech_badge('Chiplet-Based Modular Trading SoC')
    pdf.ln(10)

    pdf.sub_heading('Permanent Structural Alpha')
    pdf.tech_badge('Regulatory Capture Engine')
    pdf.tech_badge('Permanent Capital Allocation AI')
    pdf.tech_badge('Insurance Float Arbitrage System')
    pdf.tech_badge('Monopoly Detection & Acquisition Scanner')
    pdf.tech_badge('Infinite Duration Risk Models')
    pdf.tech_badge('Cash Flow Permanence Scoring')
    pdf.tech_badge('Margin of Safety Calculator (Autonomous)')
    pdf.tech_badge('Anti-Fragile Portfolio Architecture')
    pdf.tech_badge('Generational Wealth Compounding Engine')
    pdf.ln(10)

    pdf.sub_heading('Total Market Control Architecture')
    pdf.tech_badge('Cross-Asset Unified Execution Brain')
    pdf.tech_badge('Prime Brokerage Disintermediation Engine')
    pdf.tech_badge('Synthetic Prime Brokerage')
    pdf.tech_badge('Central Bank Policy Decoder')
    pdf.tech_badge('Sovereign Debt Stress Testing (190 Countries)')
    pdf.tech_badge('OTC Derivatives Pricing Supremacy')
    pdf.tech_badge('Global Liquidity Mapping Engine')
    pdf.tech_badge('Counterparty Risk Neural Network')
    pdf.tech_badge('Regulatory Arbitrage Optimiser')
    pdf.ln(10)

    pdf.sub_heading('Biomedical Alpha & Life Sciences Intelligence')
    pdf.tech_badge('Drug Pipeline Probability Engine')
    pdf.tech_badge('Clinical Trial Outcome Predictor')
    pdf.tech_badge('Patent Cliff Arbitrage System')
    pdf.tech_badge('Molecular Discovery Alpha')
    pdf.tech_badge('Healthcare Spending Topology')
    pdf.tech_badge('Biomarker Signal Intelligence')
    pdf.tech_badge('Regulatory Pathway Optimiser')
    pdf.tech_badge('GLP-1 & Obesity Economy Modelling')
    pdf.tech_badge('Longevity & Aging Alpha')
    pdf.ln(10)

    pdf.sub_heading('Energy & Geopolitical Dominance')
    pdf.tech_badge('Global Energy Flow Mapping (Real-Time)')
    pdf.tech_badge('Geopolitical Risk Pricing Engine')
    pdf.tech_badge('OPEC+ Decision Predictor')
    pdf.tech_badge('Refinery Margin Optimiser')
    pdf.tech_badge('Carbon Credit & Emissions Trading Intelligence')
    pdf.tech_badge('Strategic Petroleum Reserve Monitor')
    pdf.tech_badge('Shale Production Decline Curve AI')
    pdf.tech_badge('Energy Transition Arbitrage')
    pdf.tech_badge('Weather-Energy Nexus Engine')
    pdf.ln(10)

    pdf.sub_heading('Consumer & Supply Chain Omniscience')
    pdf.tech_badge('Global Consumer Demand Forecasting (SKU-Level)')
    pdf.tech_badge('Real-Time Freight & Logistics Pricing')
    pdf.tech_badge('Grocery & Staples Inflation Predictor')
    pdf.tech_badge('Point-of-Sale Signal Intelligence')
    pdf.tech_badge('Private Label vs Brand Switching Detector')
    pdf.tech_badge('Inventory Glut & Shortage Predictor')
    pdf.tech_badge('Agricultural Commodity Chain Modelling')
    pdf.tech_badge('Cross-Border Trade Flow Intelligence')
    pdf.tech_badge('Consumer Credit Stress Barometer')
    pdf.ln(10)

    pdf.sub_heading('Memory & Storage Supremacy')
    pdf.tech_badge('In-Memory Computing Fabric')
    pdf.tech_badge('CXL 3.0 Memory-Semantic Trading')
    pdf.tech_badge('HBM4-Native Data Structures')
    pdf.tech_badge('Persistent Memory Trading Journal')
    pdf.tech_badge('Memory-Tiered Alpha Cache')
    pdf.tech_badge('3D-Stacked Memory Accelerator')
    pdf.tech_badge('Bandwidth-Optimised Market Data Bus')
    pdf.tech_badge('Memory-Mapped Global Order Book')
    pdf.tech_badge('Cryogenic Memory Subsystem')
    pdf.ln(10)

    pdf.sub_heading('Absolute Asset Management Supremacy')
    pdf.tech_badge('Autonomous Index Construction Engine')
    pdf.tech_badge('ETF Flow Prediction System')
    pdf.tech_badge('Total Addressable Market Mapper')
    pdf.tech_badge('Unified Risk Platform (Next-Gen Aladdin)')
    pdf.tech_badge('Passive-Active Convergence Engine')
    pdf.tech_badge('Securities Lending Optimisation AI')
    pdf.tech_badge('ESG & Climate Risk Quantification (Real-Time)')
    pdf.tech_badge('Fee Compression Warfare Engine')
    pdf.tech_badge('Sovereign Wealth Fund Intelligence')
    pdf.tech_badge('Universal Ownership Model')
    pdf.ln(10)

    pdf.sub_heading('Critical Infrastructure Intelligence')
    pdf.tech_badge('Grid Frequency Deviation Alpha')
    pdf.tech_badge('Transmission Constraint Pricing')
    pdf.tech_badge('Renewable Intermittency Arbitrage')
    pdf.tech_badge('Infrastructure CapEx Cycle Predictor')
    pdf.tech_badge('Demand Response Aggregation Intelligence')
    pdf.tech_badge('Grid Resilience Stress Testing')
    pdf.ln(10)

    pdf.sub_heading('Consumer & Brand Intelligence')
    pdf.tech_badge('Brand Equity Decay Predictor')
    pdf.tech_badge('Commodity-to-Shelf Margin Modelling')
    pdf.tech_badge('Emerging Market Consumer Penetration AI')
    pdf.tech_badge('Sustainability Premium Quantification')
    pdf.ln(10)

    pdf.sub_heading('Semiconductor Fabrication Intelligence')
    pdf.tech_badge('Wafer Start & Fab Utilisation Predictor')
    pdf.tech_badge('Process Node Migration Alpha')
    pdf.tech_badge('Semiconductor Inventory Supercycle Model')
    pdf.tech_badge('Lithography Capacity Bottleneck Tracker')
    pdf.tech_badge('Advanced Packaging Demand Forecaster')
    pdf.tech_badge('Foundry Pricing Power Model')
    pdf.tech_badge('Geopolitical Semiconductor Risk Engine')
    pdf.tech_badge('Design Win Intelligence Network')
    pdf.tech_badge('Yield Curve Anomaly Detection')
    pdf.ln(10)

    pdf.sub_heading('Sovereign Resource Dominance')
    pdf.tech_badge('Global Crude Grade Arbitrage Engine')
    pdf.tech_badge('Petrochemical Value Chain Optimiser')
    pdf.tech_badge('Oil Field Decline Rate Intelligence')
    pdf.tech_badge('Tanker Fleet Tracking & Voyage Prediction')
    pdf.tech_badge('Strategic Reserve & Spare Capacity Model')
    pdf.tech_badge('Downstream Demand Destruction Predictor')
    pdf.tech_badge('Sovereign Investment Fund Flow Tracker')
    pdf.tech_badge('LNG Spot Market Arbitrage')
    pdf.tech_badge('Peak Oil Demand Timing Model')
    pdf.ln(10)

    pdf.sub_heading('Institutional Trading Supremacy')
    pdf.tech_badge('Flow Toxicity Analyser (VPIN)')
    pdf.tech_badge('Dark Pool Dominance Engine')
    pdf.tech_badge('Systematic Market Making (All Asset Classes)')
    pdf.tech_badge('IPO & Issuance Pricing Oracle')
    pdf.tech_badge('M&A Arbitrage Intelligence')
    pdf.tech_badge('Credit Default Prediction (500ms)')
    pdf.tech_badge('Rates & Yield Curve Arbitrage')
    pdf.tech_badge('FX Microstructure Exploitation')
    pdf.tech_badge('Structured Products Auto-Pricer')
    pdf.ln(10)

    pdf.sub_heading('Global Payment Network Intelligence')
    pdf.tech_badge('Real-Time Transaction Velocity Mapping')
    pdf.tech_badge('Cross-Border Payment Flow Alpha')
    pdf.tech_badge('Merchant Revenue Nowcasting')
    pdf.tech_badge('Fraud Pattern Alpha Extraction')
    pdf.tech_badge('Buy Now Pay Later Stress Index')
    pdf.tech_badge('Digital Wallet Adoption Curve Modelling')
    pdf.tech_badge('Interchange Fee Regulatory Predictor')
    pdf.tech_badge('Real-Time GDP Proxy (180 Countries)')
    pdf.tech_badge('Crypto & Stablecoin Substitution Tracker')
    pdf.ln(10)

    pdf.sub_heading('On-Chain Omniscience & Digital Asset Dominance')
    pdf.tech_badge('Whale Wallet Clustering & Tracking')
    pdf.tech_badge('MEV Extraction & Protection Engine')
    pdf.tech_badge('DeFi Protocol Risk Scoring (Real-Time)')
    pdf.tech_badge('Cross-Chain Liquidity Arbitrage')
    pdf.tech_badge('Stablecoin De-Peg Early Warning')
    pdf.tech_badge('On-Chain Derivatives Intelligence')
    pdf.tech_badge('Token Unlock & Vesting Cliff Predictor')
    pdf.tech_badge('Regulatory Classification Engine')
    pdf.tech_badge('Bitcoin Miner Economics Model')
    pdf.ln(10)

    pdf.sub_heading('Healthcare System Omniscience')
    pdf.tech_badge('Claims Trajectory Predictor')
    pdf.tech_badge('Prescription Volume Nowcasting')
    pdf.tech_badge('Hospital Utilisation & Bed Occupancy Model')
    pdf.tech_badge('Medicare Advantage Enrolment Predictor')
    pdf.tech_badge('PBM Rebate & Formulary Alpha')
    pdf.tech_badge('Telehealth Adoption & Cannibalisation Model')
    pdf.tech_badge('Value-Based Care Outcome Predictor')
    pdf.tech_badge('Medical Device Adoption Curve Intelligence')
    pdf.tech_badge('Healthcare Workforce Shortage Alpha')
    pdf.ln(10)

    pdf.sub_heading('GLP-1 & Metabolic Revolution Intelligence')
    pdf.tech_badge('GLP-1 Prescription Trajectory Model (Global)')
    pdf.tech_badge('Obesity Treatment Penetration Curve')
    pdf.tech_badge('GLP-1 Supply Constraint Predictor')
    pdf.tech_badge('Compounding Pharmacy Threat Quantifier')
    pdf.tech_badge('Payer Coverage & Formulary Shift Tracker')
    pdf.tech_badge('Metabolic Disease Cascade Modelling')
    pdf.tech_badge('Competitive Pipeline Threat Assessment')
    pdf.tech_badge('Weight Regain & Adherence Predictor')
    pdf.tech_badge('GLP-1 Economic Ripple Effect Engine')
    pdf.ln(10)

    pdf.sub_heading('Defence & Classified Intelligence Superiority')
    pdf.tech_badge('Global Defence Spending Predictor')
    pdf.tech_badge('Weapons Program Lifecycle Model')
    pdf.tech_badge('Geopolitical Conflict Probability Engine')
    pdf.tech_badge('Classified Contract Revenue Estimator')
    pdf.tech_badge('Satellite Constellation Threat Assessment')
    pdf.tech_badge('Hypersonic & Missile Defence Market Model')
    pdf.tech_badge('Defence Supply Chain Vulnerability Scanner')
    pdf.tech_badge('NATO & Alliance Spending Compliance Tracker')
    pdf.tech_badge('Veteran & Cleared Workforce Intelligence')
    pdf.ln(10)

    pdf.sub_heading('Adversarial Intelligence Platform Supremacy')
    pdf.tech_badge('Gotham-Class Financial Intelligence Graph')
    pdf.tech_badge('Foundry-Class Data Integration (Zero ETL)')
    pdf.tech_badge('Adversarial Entity Resolution Engine')
    pdf.tech_badge('Predictive Threat Intelligence (Financial)')
    pdf.tech_badge('Autonomous Decision Intelligence')
    pdf.tech_badge('Temporal Causal Reasoning Engine')
    pdf.tech_badge('Counter-Surveillance Detection System')
    pdf.tech_badge('Multi-Classification Data Fusion')
    pdf.tech_badge('Human-on-the-Loop Escalation Architecture')
    pdf.ln(10)

    pdf.sub_heading('Lithography Monopoly Intelligence')
    pdf.tech_badge('EUV Throughput Yield Prediction')
    pdf.tech_badge('Lithography Capex Allocation Engine')
    pdf.tech_badge('Semiconductor Equipment Supply Chain Graph')
    pdf.tech_badge('Geopolitical Export Control Modelling')
    pdf.tech_badge('Installed Base Utilisation Intelligence')
    pdf.tech_badge('Photon-to-Revenue Attribution Model')
    pdf.tech_badge('High-NA EUV Adoption Forecasting')
    pdf.tech_badge('Metrology-Driven Defect Economics')
    pdf.tech_badge('Litho Monopoly Moat Quantification')
    pdf.ln(10)

    pdf.sub_heading('Heterogeneous Compute Supremacy')
    pdf.tech_badge('ROCm-Native Model Training Pipeline')
    pdf.tech_badge('EPYC Core-per-Dollar Alpha Engine')
    pdf.tech_badge('Chiplet Architecture Cost Modelling')
    pdf.tech_badge('FPGA Adaptive Trading Fabric')
    pdf.tech_badge('GPU Compute TCO Arbitrage')
    pdf.tech_badge('Heterogeneous Compute Orchestrator')
    pdf.tech_badge('AMD vs NVIDIA Market Share Predictor')
    pdf.tech_badge('Infinity Fabric Interconnect Intelligence')
    pdf.tech_badge('Open-Source Compute Ecosystem Tracker')
    pdf.ln(10)

    pdf.sub_heading('Luxury & Desire Intelligence')
    pdf.tech_badge('Ultra-High-Net-Worth Spending Predictor')
    pdf.tech_badge('Luxury Brand Sentiment Thermometer')
    pdf.tech_badge('Scarcity & Waitlist Pricing Engine')
    pdf.tech_badge('Chinese Consumer Luxury Appetite Model')
    pdf.tech_badge('Aspirational-to-Affluent Conversion Tracker')
    pdf.tech_badge('Counterfeit & Grey Market Intelligence')
    pdf.tech_badge('Fashion Trend Cycle Predictor')
    pdf.tech_badge('Luxury Real Estate & Tourism Correlation Engine')
    pdf.tech_badge('Succession & Conglomerate M&A Intelligence')
    pdf.ln(10)

    pdf.sub_heading('Heavy Industry & Earth Intelligence')
    pdf.tech_badge('Global Construction Activity Nowcaster')
    pdf.tech_badge('Mining Capex Cycle Predictor')
    pdf.tech_badge('Equipment Utilisation & Idle Fleet Tracker')
    pdf.tech_badge('Commodity-to-Machine Demand Model')
    pdf.tech_badge('Infrastructure Stimulus Pipeline Intelligence')
    pdf.tech_badge('Dealer Network Health Scoring')
    pdf.tech_badge('Autonomous Mining Fleet Economics')
    pdf.tech_badge('Energy Transition Equipment Demand Forecaster')
    pdf.tech_badge('Machine Lifecycle & Rebuild Economics')
    pdf.ln(10)

    pdf.sub_heading('Resource Extraction Omniscience')
    pdf.tech_badge('Ore Body Valuation Engine')
    pdf.tech_badge('Commodity Super-Cycle Detector')
    pdf.tech_badge('Autonomous Mine-to-Port Optimiser')
    pdf.tech_badge('Water & Tailings Risk Quantifier')
    pdf.tech_badge('Critical Minerals Supply Gap Forecaster')
    pdf.tech_badge('ESG & Decarbonisation Cost Modelling')
    pdf.tech_badge('Geopolitical Resource Nationalism Tracker')
    pdf.tech_badge('Processing & Smelting Margin Intelligence')
    pdf.tech_badge('Exploration Target Probability Scoring')
    pdf.ln(10)

    pdf.sub_heading('China Digital Economy Supremacy')
    pdf.tech_badge('WeChat/Alipay Transaction Flow Intelligence')
    pdf.tech_badge('China A-Share Retail Sentiment Decoder')
    pdf.tech_badge('Cross-Border Capital Flow Tracker (CNY)')
    pdf.tech_badge('Alibaba Cloud vs Hyperscaler Market Model')
    pdf.tech_badge('Chinese Regulatory Crackdown Predictor')
    pdf.tech_badge('Singles\' Day / 618 Economic Barometer')
    pdf.tech_badge('China Tech ADR De-Listing Risk Scorer')
    pdf.tech_badge('Southeast Asia Super-App Expansion Tracker')
    pdf.tech_badge('China Property Contagion Engine')
    pdf.ln(10)

    pdf.sub_heading('Vertical Integration Empire Intelligence')
    pdf.tech_badge('DRAM/NAND Pricing Cycle Predictor')
    pdf.tech_badge('Foundry Node Race Intelligence')
    pdf.tech_badge('Galaxy Ecosystem Monetisation Model')
    pdf.tech_badge('Display Technology Dominance Tracker')
    pdf.tech_badge('Chaebol Cross-Subsidy Analyser')
    pdf.tech_badge('HBM Capacity & Allocation Intelligence')
    pdf.tech_badge('Smartphone Market Share Erosion Model')
    pdf.tech_badge('South Korea Macro & Won Sensitivity Engine')
    pdf.tech_badge('Vertical Integration Margin Optimiser')
    pdf.ln(10)

    pdf.sub_heading('Palantir-Killer Intelligence Supremacy')
    pdf.tech_badge('Self-Building Ontology Engine')
    pdf.tech_badge('Zero-Deployment Intelligence Platform')
    pdf.tech_badge('Autonomous Action Execution (Not Just Dashboards)')
    pdf.tech_badge('Real-Time Financial Alpha Generation')
    pdf.tech_badge('Predictive-First Architecture (Not Retrospective)')
    pdf.tech_badge('Adversarial AI Red-Teaming Engine')
    pdf.tech_badge('Sovereign-Grade Privacy Without Lock-In')
    pdf.tech_badge('Democratic Pricing Model')
    pdf.tech_badge('Multi-Domain Fusion Without Silos')
    pdf.ln(10)

    pdf.sub_heading('Structural Palantir Superiority')
    pdf.tech_badge('Live Market Microstructure Engine')
    pdf.tech_badge('Cross-Asset Contagion Propagation Model')
    pdf.tech_badge('Generative Scenario Simulation (Not Static Ontology)')
    pdf.tech_badge('Regulatory Arbitrage Intelligence')
    pdf.tech_badge('Natural Language Strategy Compiler')
    pdf.tech_badge('Continuous Model Evolution (Not Version Releases)')
    pdf.tech_badge('Embedded Compliance-as-Code')
    pdf.tech_badge('Financial Knowledge Graph (Not Generic Ontology)')
    pdf.tech_badge('Latency-Optimised Architecture')
    pdf.ln(10)

    pdf.sub_heading('Security & Observability')
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
