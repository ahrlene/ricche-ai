"""
Generate three professional PDFs for Ricche Ltd website:
1. Architecture Diagram Pack
2. AI Platform Overview Poster
3. Control Room Dashboard Mockup
"""

from fpdf import FPDF
import os

NAVY = (14, 17, 30)
DARK = (26, 26, 46)
BODY_COLOR = (50, 50, 60)
ACCENT = (59, 130, 246)      # Blue accent
NVIDIA_GREEN = (118, 185, 0)  # NVIDIA green
LIGHT_BG = (235, 238, 245)
WHITE = (255, 255, 255)
GRAY = (140, 140, 150)
BORDER_COLOR = (200, 205, 215)

OUT_DIR = os.path.dirname(__file__)


class RicchePDF(FPDF):
    """Base PDF class with Ricche branding."""

    def __init__(self, title_text, subtitle_text):
        super().__init__()
        self.title_text = title_text
        self.subtitle_text = subtitle_text
        self.set_auto_page_break(auto=True, margin=20)

    def dark_header_bar(self):
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 38, 'F')
        self.set_xy(15, 10)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(*WHITE)
        self.cell(0, 6, 'RICCHE', new_x='LMARGIN', new_y='NEXT')
        self.set_xy(15, 18)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(180, 185, 200)
        self.cell(0, 5, 'AI Research Infrastructure for Financial Markets', new_x='LMARGIN', new_y='NEXT')
        # Blue accent line
        self.set_fill_color(*ACCENT)
        self.rect(0, 38, 210, 1.5, 'F')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 7)
        self.set_text_color(*GRAY)
        self.cell(0, 8, f'Ricche Ltd  |  ricche.ai  |  Confidential', align='C')

    def title_page(self):
        self.add_page()
        self.dark_header_bar()
        self.ln(60)
        self.set_font('Helvetica', 'B', 28)
        self.set_text_color(*DARK)
        self.cell(0, 14, self.title_text, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(6)
        self.set_font('Helvetica', '', 13)
        self.set_text_color(*GRAY)
        self.cell(0, 8, self.subtitle_text, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(8)
        # Thin rule
        self.set_draw_color(*BORDER_COLOR)
        self.line(60, self.get_y(), 150, self.get_y())
        self.ln(8)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(*GRAY)
        self.cell(0, 6, 'Ricche Ltd  |  ricche.ai', align='C', new_x='LMARGIN', new_y='NEXT')
        self.cell(0, 6, 'GPU-Accelerated AI Infrastructure', align='C', new_x='LMARGIN', new_y='NEXT')

    def content_page(self):
        self.add_page()
        self.dark_header_bar()
        self.set_y(48)

    def section_heading(self, text):
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(*DARK)
        self.ln(4)
        self.cell(0, 9, text, new_x='LMARGIN', new_y='NEXT')
        # Accent underline
        self.set_fill_color(*ACCENT)
        self.rect(self.l_margin, self.get_y(), 30, 0.8, 'F')
        self.ln(6)

    def sub_heading(self, text):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(*DARK)
        self.ln(2)
        self.cell(0, 7, text, new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

    def body(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(*BODY_COLOR)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(*BODY_COLOR)
        x = self.l_margin
        self.set_x(x)
        self.cell(8, 5.5, '  -  ', new_x='END', new_y='TOP')
        self.multi_cell(0, 5.5, text)

    def nvidia_badge(self, text):
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(230, 245, 210)
        self.set_text_color(80, 130, 0)
        w = self.get_string_width(text) + 8
        self.cell(w, 7, text, new_x='END', new_y='TOP', fill=True)
        self.cell(3, 7, '')  # spacer

    def tech_badge(self, text):
        self.set_font('Helvetica', '', 8)
        self.set_fill_color(*LIGHT_BG)
        self.set_text_color(*BODY_COLOR)
        w = self.get_string_width(text) + 6
        self.cell(w, 6, text, new_x='END', new_y='TOP', fill=True)
        self.cell(2, 6, '')

    def card_box(self, title, body_text, x, y, w=82, h=45):
        self.set_fill_color(*LIGHT_BG)
        self.set_draw_color(*BORDER_COLOR)
        self.rect(x, y, w, h, 'DF')
        # Card top accent
        self.set_fill_color(*ACCENT)
        self.rect(x, y, w, 1.5, 'F')
        self.set_xy(x + 4, y + 5)
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(*DARK)
        self.cell(w - 8, 5, title, new_x='LMARGIN', new_y='NEXT')
        self.set_xy(x + 4, y + 13)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*BODY_COLOR)
        self.multi_cell(w - 8, 4.2, body_text)

    def nvidia_card_box(self, title, body_text, x, y, w=82, h=45):
        self.set_fill_color(*LIGHT_BG)
        self.set_draw_color(*BORDER_COLOR)
        self.rect(x, y, w, h, 'DF')
        # NVIDIA green top accent
        self.set_fill_color(*NVIDIA_GREEN)
        self.rect(x, y, w, 1.5, 'F')
        self.set_xy(x + 4, y + 5)
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(80, 130, 0)
        self.cell(w - 8, 5, title, new_x='LMARGIN', new_y='NEXT')
        self.set_xy(x + 4, y + 13)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*BODY_COLOR)
        self.multi_cell(w - 8, 4.2, body_text)

    def flow_arrow(self, steps, y):
        """Draw a horizontal flow diagram."""
        n = len(steps)
        box_w = 30
        gap = (170 - n * box_w) / max(n - 1, 1)
        x = 20
        for i, step in enumerate(steps):
            self.set_fill_color(*LIGHT_BG)
            self.set_draw_color(*ACCENT)
            self.rect(x, y, box_w, 14, 'DF')
            self.set_xy(x + 1, y + 2)
            self.set_font('Helvetica', '', 7)
            self.set_text_color(*DARK)
            self.multi_cell(box_w - 2, 3.5, step, align='C')
            if i < n - 1:
                # Arrow
                ax = x + box_w + 1
                ay = y + 7
                self.set_draw_color(*ACCENT)
                self.line(ax, ay, ax + gap - 2, ay)
                # arrowhead
                self.line(ax + gap - 5, ay - 2, ax + gap - 2, ay)
                self.line(ax + gap - 5, ay + 2, ax + gap - 2, ay)
            x += box_w + gap

    def stat_box(self, value, label, x, y, w=40):
        self.set_fill_color(*NAVY)
        self.rect(x, y, w, 22, 'F')
        self.set_xy(x, y + 3)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*ACCENT)
        self.cell(w, 7, value, align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_xy(x, y + 12)
        self.set_font('Helvetica', '', 7)
        self.set_text_color(180, 185, 200)
        self.cell(w, 5, label, align='C')


# ==============================================================
# PDF 1: Architecture Diagram Pack
# ==============================================================
def generate_architecture_pdf():
    pdf = RicchePDF('Architecture Diagram Pack', 'Platform Architecture, Research Workflow & Compute Infrastructure')
    pdf.title_page()

    # --- Page 2: High-Level System Architecture ---
    pdf.content_page()
    pdf.section_heading('1. High-Level System Architecture')
    pdf.body(
        'The Ricche platform is designed as a multi-layered research infrastructure '
        'connecting market data sources to machine learning experimentation, simulation, '
        'and validation systems. Each layer is purpose-built for quantitative financial research.'
    )

    # Flow diagram
    pdf.flow_arrow(['Market Data\nIngestion', 'Data\nInfrastructure', 'ML Research\nEnvironment', 'Simulation\nFramework', 'Validation\n& Governance'], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Core Architecture Layers')
    pdf.card_box(
        'Data Ingestion Layer',
        'Real-time and historical market data feeds from major exchanges. '
        'Tick-level order books, OHLCV, economic indicators, and alternative data. '
        'Quality checks, normalisation, and time-series alignment.',
        15, pdf.get_y(), 85, 38
    )
    pdf.card_box(
        'Compute & Storage Layer',
        'NVIDIA GPU clusters for ML training and simulation workloads. '
        'Distributed storage with columnar formats (Parquet, Arrow). '
        'Auto-scaling compute allocation based on workload priority.',
        110, pdf.get_y(), 85, 38
    )
    pdf.ln(42)

    pdf.card_box(
        'Research & Experimentation Layer',
        'Experiment tracking, model versioning, and reproducible pipelines. '
        'CUDA-accelerated PyTorch environments for model development. '
        'Hyperparameter optimisation and feature engineering frameworks.',
        15, pdf.get_y(), 85, 38
    )
    pdf.card_box(
        'Monitoring & Observability',
        'Real-time system dashboards tracking GPU utilisation, pipeline health, '
        'data freshness, and experiment progress. Alerting for anomalies '
        'and infrastructure issues.',
        110, pdf.get_y(), 85, 38
    )
    pdf.ln(42)

    # --- Page 3: GPU Compute Infrastructure ---
    pdf.content_page()
    pdf.section_heading('2. GPU Compute Infrastructure')
    pdf.body(
        'Training and simulation workloads run on NVIDIA GPU clusters optimised for '
        'high-throughput numerical computation. The compute layer leverages the full '
        'NVIDIA accelerated computing stack.'
    )
    pdf.ln(2)

    # NVIDIA tech badges
    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS cuDF')
    pdf.nvidia_badge('Triton Inference')
    pdf.nvidia_badge('cuML')
    pdf.ln(12)

    pdf.nvidia_card_box(
        'NVIDIA CUDA Training Clusters',
        'Multi-GPU training environments using CUDA-accelerated PyTorch. '
        'Mixed-precision training (FP16/BF16) for faster convergence. '
        'Distributed data-parallel training across GPU nodes. '
        'Up to 47x faster model training vs. CPU-only baselines.',
        15, pdf.get_y(), 85, 48
    )
    pdf.nvidia_card_box(
        'RAPIDS Data Processing',
        'GPU-accelerated data pipelines using RAPIDS cuDF for DataFrame operations. '
        'End-to-end GPU processing eliminates CPU-GPU transfer bottlenecks. '
        'Accelerated feature engineering for time-series financial data. '
        'Seamless integration with PyTorch training pipelines.',
        110, pdf.get_y(), 85, 48
    )
    pdf.ln(52)

    pdf.nvidia_card_box(
        'TensorRT Inference Optimisation',
        'Trained models are optimised using NVIDIA TensorRT for production inference. '
        'Layer fusion, kernel auto-tuning, and precision calibration. '
        'Sub-2ms inference latency for real-time signal generation. '
        'INT8 quantisation with minimal accuracy loss.',
        15, pdf.get_y(), 85, 45
    )
    pdf.nvidia_card_box(
        'Triton Inference Server',
        'Model serving via NVIDIA Triton for concurrent multi-model inference. '
        'Dynamic batching and model ensembles for throughput optimisation. '
        'GPU memory management across simultaneous model deployments. '
        'gRPC and REST endpoints for research pipeline integration.',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(50)

    # Performance stats
    pdf.stat_box('47x', 'GPU vs CPU Training', 20, pdf.get_y(), 50)
    pdf.stat_box('<2ms', 'Inference Latency', 80, pdf.get_y(), 50)
    pdf.stat_box('10B+', 'Data Points Processed', 140, pdf.get_y(), 50)
    pdf.ln(28)

    # --- Page 4: Data Pipeline Architecture ---
    pdf.content_page()
    pdf.section_heading('3. Data Pipeline Architecture')
    pdf.body(
        'Market data flows through a multi-stage ingestion pipeline designed for reliability, '
        'low latency, and data quality assurance. The pipeline supports both real-time streaming '
        'and historical batch processing.'
    )

    pdf.flow_arrow(['Exchange\nFeeds', 'Ingestion\nGateway', 'Quality\nChecks', 'Normalisation\n& Alignment', 'Feature\nStore'], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Data Sources & Coverage')
    pdf.bullet('Global equities, futures (including commodities), options, FX, and fixed income')
    pdf.bullet('Tick-level order book data from major exchanges (NYSE, CME, LSE, Eurex, HKEX)')
    pdf.bullet('End-of-day pricing, corporate actions, and reference data')
    pdf.bullet('Economic indicators, central bank releases, and macro datasets')
    pdf.bullet('Alternative data: satellite imagery, NLP-processed news, sentiment signals')
    pdf.ln(4)

    pdf.sub_heading('Pipeline Characteristics')
    pdf.card_box(
        'Streaming Ingestion',
        'Low-latency real-time feeds processed through event-driven pipelines. '
        'Message queuing with exactly-once semantics. Automatic reconnection '
        'and gap detection for exchange feeds.',
        15, pdf.get_y(), 85, 38
    )
    pdf.card_box(
        'Batch Processing',
        'Scheduled batch pipelines for historical data backfills and daily reconciliation. '
        'GPU-accelerated data transforms using RAPIDS cuDF. '
        'Idempotent processing with full audit trails.',
        110, pdf.get_y(), 85, 38
    )
    pdf.ln(42)

    # --- Page 5: Research Workflow ---
    pdf.content_page()
    pdf.section_heading('4. Research Workflow Architecture')
    pdf.body(
        'The research workflow is structured to support disciplined, reproducible experimentation. '
        'Each stage is tracked, versioned, and auditable, enabling teams to iterate on hypotheses '
        'with confidence.'
    )

    pdf.flow_arrow(['Research\nHypothesis', 'Data\nPreparation', 'Model\nDevelopment', 'Simulation\nTesting', 'Validation\n& Review'], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Stage 1: Research Hypothesis')
    pdf.body(
        'Researchers define hypotheses about market behaviour, specifying target instruments, '
        'timeframes, and expected signal characteristics. Hypotheses are registered in the '
        'experiment tracking system with metadata and success criteria.'
    )

    pdf.sub_heading('Stage 2: Data Preparation')
    pdf.body(
        'Relevant datasets are extracted from the feature store and prepared for modelling. '
        'GPU-accelerated feature engineering using RAPIDS produces training-ready datasets '
        'with proper train/validation/test splits and temporal consistency.'
    )

    pdf.sub_heading('Stage 3: Model Development')
    pdf.body(
        'Models are developed in CUDA-accelerated PyTorch environments on NVIDIA GPU clusters. '
        'Experiment tracking captures hyperparameters, metrics, and model artifacts. '
        'Automated hyperparameter search explores the configuration space efficiently.'
    )

    pdf.sub_heading('Stage 4: Simulation Testing')
    pdf.body(
        'Candidate models are evaluated in GPU-parallelised simulation environments. '
        'Monte Carlo simulations test behaviour across thousands of market scenarios. '
        'Agent-based simulations model market microstructure interactions.'
    )

    pdf.sub_heading('Stage 5: Validation & Review')
    pdf.body(
        'Models passing simulation are subject to out-of-sample validation, stress testing, '
        'and peer review. Statistical significance tests guard against overfitting. '
        'Approved models enter controlled evaluation with position-size constraints.'
    )

    # --- Page 6: Technology Stack ---
    pdf.content_page()
    pdf.section_heading('5. Technology Stack')
    pdf.body('The platform is built on industry-standard open-source and enterprise technologies:')
    pdf.ln(2)

    pdf.sub_heading('Compute & GPU')
    pdf.nvidia_badge('NVIDIA CUDA')
    pdf.nvidia_badge('TensorRT')
    pdf.nvidia_badge('RAPIDS')
    pdf.nvidia_badge('Triton')
    pdf.ln(10)

    pdf.sub_heading('Machine Learning')
    pdf.tech_badge('PyTorch')
    pdf.tech_badge('scikit-learn')
    pdf.tech_badge('XGBoost')
    pdf.tech_badge('Optuna')
    pdf.tech_badge('MLflow')
    pdf.ln(10)

    pdf.sub_heading('Data Engineering')
    pdf.tech_badge('Apache Kafka')
    pdf.tech_badge('Apache Arrow')
    pdf.tech_badge('Parquet')
    pdf.tech_badge('PostgreSQL')
    pdf.tech_badge('Redis')
    pdf.ln(10)

    pdf.sub_heading('Infrastructure')
    pdf.tech_badge('Kubernetes')
    pdf.tech_badge('Docker')
    pdf.tech_badge('Terraform')
    pdf.tech_badge('Prometheus')
    pdf.tech_badge('Grafana')
    pdf.ln(10)

    pdf.sub_heading('Languages')
    pdf.tech_badge('Python')
    pdf.tech_badge('Rust')
    pdf.tech_badge('SQL')
    pdf.tech_badge('CUDA C++')
    pdf.ln(14)

    pdf.body(
        'This technology stack is designed for performance, reliability, and researcher productivity. '
        'Infrastructure-as-code ensures reproducible deployments, while containerised workloads '
        'enable efficient resource utilisation across the GPU cluster.'
    )

    out = os.path.join(OUT_DIR, 'ricche_architecture_diagram_pack.pdf')
    pdf.output(out)
    print(f'Architecture Diagram Pack: {out} ({os.path.getsize(out):,} bytes)')


# ==============================================================
# PDF 2: AI Platform Overview Poster
# ==============================================================
def generate_overview_pdf():
    pdf = RicchePDF('AI Platform Overview', 'GPU-Accelerated Research Infrastructure for Quantitative Markets')
    pdf.title_page()

    # --- Page 2: Platform at a Glance ---
    pdf.content_page()
    pdf.section_heading('Platform at a Glance')
    pdf.body(
        'Ricche is building GPU-accelerated AI research infrastructure designed to explore '
        'financial markets through machine learning, computational modelling, and large-scale '
        'data analysis. The platform enables disciplined, reproducible research across the full '
        'quantitative research lifecycle.'
    )
    pdf.ln(2)

    # Stats row
    pdf.stat_box('47x', 'GPU Acceleration', 15, pdf.get_y(), 42)
    pdf.stat_box('<2ms', 'Inference Latency', 62, pdf.get_y(), 42)
    pdf.stat_box('10B+', 'Data Points', 109, pdf.get_y(), 42)
    pdf.stat_box('24/7', 'Monitoring', 156, pdf.get_y(), 38)
    pdf.ln(30)

    pdf.section_heading('Core Capabilities')

    pdf.card_box(
        'Machine Learning Research',
        'NVIDIA CUDA-accelerated model training on GPU clusters. '
        'PyTorch-based experimentation with full experiment tracking, '
        'hyperparameter optimisation, and model versioning. '
        'Supports deep learning, gradient boosting, and ensemble methods.',
        15, pdf.get_y(), 85, 48
    )
    pdf.card_box(
        'Simulation Engines',
        'GPU-parallelised Monte Carlo simulations and agent-based models. '
        'Test strategies across thousands of market scenarios in minutes. '
        'Configurable market microstructure and regime dynamics. '
        'Statistical validation of simulation outputs.',
        110, pdf.get_y(), 85, 48
    )
    pdf.ln(52)

    pdf.card_box(
        'Data Infrastructure',
        'Multi-asset market data ingestion spanning equities, futures, options, '
        'FX, and fixed income. Real-time streaming and historical batch '
        'pipelines. GPU-accelerated feature engineering with RAPIDS cuDF. '
        'Comprehensive data quality and reconciliation framework.',
        15, pdf.get_y(), 85, 48
    )
    pdf.card_box(
        'Monitoring & Observability',
        'Real-time dashboards tracking GPU utilisation, training experiments, '
        'simulation queues, and pipeline throughput. Automated alerting '
        'for infrastructure anomalies and data quality issues. '
        'Full audit trail for research governance.',
        110, pdf.get_y(), 85, 48
    )
    pdf.ln(52)

    # --- Page 3: NVIDIA Technology Stack ---
    pdf.content_page()
    pdf.section_heading('NVIDIA Accelerated Computing Stack')
    pdf.body(
        'The platform is powered by the NVIDIA GPU ecosystem, delivering orders-of-magnitude '
        'performance gains across data processing, model training, and inference workloads.'
    )
    pdf.ln(2)

    pdf.nvidia_card_box(
        'NVIDIA CUDA',
        'Foundation of the compute layer. All training and simulation workloads leverage '
        'CUDA-accelerated kernels for maximum throughput. Mixed-precision training with '
        'FP16/BF16 for faster convergence without sacrificing model quality.',
        15, pdf.get_y(), 85, 45
    )
    pdf.nvidia_card_box(
        'RAPIDS cuDF',
        'GPU-accelerated DataFrames for data engineering at scale. End-to-end GPU '
        'processing eliminates CPU-GPU transfer overhead. Feature engineering for '
        'financial time-series runs 10-50x faster than pandas equivalents.',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(50)

    pdf.nvidia_card_box(
        'TensorRT',
        'Production inference optimisation through layer fusion, kernel auto-tuning, '
        'and precision calibration. Delivers sub-2ms latency for real-time signal '
        'generation. INT8 quantisation for deployment efficiency.',
        15, pdf.get_y(), 85, 42
    )
    pdf.nvidia_card_box(
        'Triton Inference Server',
        'Scalable model serving supporting concurrent multi-model inference. Dynamic '
        'batching optimises GPU utilisation. Supports PyTorch, TensorRT, and ONNX '
        'model formats with gRPC and REST APIs.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(48)

    # --- Page 4: Market Coverage & Research ---
    pdf.content_page()
    pdf.section_heading('Market Coverage')
    pdf.body(
        'The data infrastructure supports global financial markets with institutional-grade '
        'data quality and coverage:'
    )
    pdf.ln(2)
    pdf.bullet('Global equities across developed and emerging markets')
    pdf.bullet('Futures (including commodities) - energy, metals, agriculture, financial futures')
    pdf.bullet('Listed options with full chain data')
    pdf.bullet('Foreign exchange - spot, forwards, and crosses')
    pdf.bullet('Fixed income - government bonds, credit, and rates')
    pdf.bullet('Alternative data - sentiment, satellite, NLP-processed news')
    pdf.ln(6)

    pdf.section_heading('Research Approach')
    pdf.body(
        'Ricche takes a disciplined, hypothesis-driven approach to quantitative research. '
        'Every experiment is tracked, versioned, and reproducible. Models progress through '
        'structured validation stages before entering controlled evaluation.'
    )
    pdf.ln(2)
    pdf.flow_arrow(['Hypothesis', 'Data Prep', 'Model Dev', 'Simulation', 'Validation'], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.section_heading('Collaboration')
    pdf.body(
        'Ricche welcomes collaboration with organisations at the intersection of artificial '
        'intelligence, quantitative finance, and high-performance computing. We are particularly '
        'interested in partnerships with technology providers, data vendors, and research institutions.'
    )
    pdf.ln(4)
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 8, 'Contact: info@ricche.ai  |  ricche.ai', align='C')

    out = os.path.join(OUT_DIR, 'ricche_ai_platform_overview_poster.pdf')
    pdf.output(out)
    print(f'AI Platform Overview: {out} ({os.path.getsize(out):,} bytes)')


# ==============================================================
# PDF 3: Control Room Dashboard Mockup
# ==============================================================
def generate_dashboard_pdf():
    pdf = RicchePDF('Control Room Dashboard', 'Real-Time Operations Monitoring & Infrastructure Health')
    pdf.title_page()

    # --- Page 2: Dashboard Overview ---
    pdf.content_page()
    pdf.section_heading('Operations Dashboard Overview')
    pdf.body(
        'The Ricche Control Room provides real-time visibility into all platform operations, '
        'from GPU compute utilisation to data pipeline health and research experiment progress. '
        'The dashboard is designed for infrastructure operators and research leads.'
    )
    pdf.ln(2)

    # Key metrics row
    pdf.stat_box('94.2%', 'GPU Utilisation', 15, pdf.get_y(), 42)
    pdf.stat_box('1,247', 'Active Experiments', 62, pdf.get_y(), 42)
    pdf.stat_box('3.2M', 'Events / sec', 109, pdf.get_y(), 42)
    pdf.stat_box('99.97%', 'Uptime (30d)', 156, pdf.get_y(), 38)
    pdf.ln(30)

    pdf.section_heading('Dashboard Panels')

    # GPU Monitoring Panel
    pdf.card_box(
        'GPU Cluster Monitoring',
        'Real-time GPU utilisation across all nodes. Per-GPU memory allocation, '
        'temperature, and power draw. CUDA kernel execution metrics. '
        'Training job queue depth and estimated completion times. '
        'Automatic alerts for thermal throttling or hardware faults.',
        15, pdf.get_y(), 85, 52
    )
    pdf.card_box(
        'Training Experiments Tracker',
        'Live view of all active ML training experiments. Loss curves, learning '
        'rate schedules, and validation metrics in real time. Resource allocation '
        'per experiment (GPUs, memory, storage). Experiment comparison and '
        'historical performance trends.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    pdf.card_box(
        'Data Pipeline Health',
        'Feed-by-feed ingestion status with latency and throughput metrics. '
        'Data quality scores and anomaly detection alerts. Gap detection and '
        'automatic backfill tracking. Historical data freshness trends '
        'across all asset classes and exchanges.',
        15, pdf.get_y(), 85, 48
    )
    pdf.card_box(
        'Simulation Queue Monitor',
        'Monte Carlo and agent-based simulation job status. Queue depth, '
        'estimated runtimes, and GPU allocation per job. Simulation result '
        'summaries with pass/fail indicators. Historical simulation throughput '
        'and resource utilisation trends.',
        110, pdf.get_y(), 85, 48
    )
    pdf.ln(52)

    # --- Page 3: Detailed Panels ---
    pdf.content_page()
    pdf.section_heading('Infrastructure Monitoring')

    pdf.card_box(
        'Compute Resource Allocation',
        'Kubernetes cluster overview showing pod status, resource requests vs. limits, '
        'and node health. GPU scheduling queue with priority levels. Auto-scaling '
        'history and projected capacity requirements.',
        15, pdf.get_y(), 85, 45
    )
    pdf.card_box(
        'Storage & Network',
        'Distributed storage utilisation across hot, warm, and cold tiers. '
        'Network throughput between compute nodes and storage. Data replication '
        'status and backup health. I/O latency percentiles (p50, p95, p99).',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(50)

    pdf.card_box(
        'Model Serving (Triton)',
        'NVIDIA Triton Inference Server monitoring. Requests per second, inference '
        'latency distributions, and batch utilisation. Per-model GPU memory footprint. '
        'Model version deployment status and rollback tracking.',
        15, pdf.get_y(), 85, 45
    )
    pdf.card_box(
        'Alerts & Incidents',
        'Active alert dashboard with severity classification (P1-P4). Mean time to '
        'detection (MTTD) and resolution (MTTR) metrics. Alert routing and '
        'on-call assignment. Incident timeline with root cause annotations.',
        110, pdf.get_y(), 85, 45
    )
    pdf.ln(50)

    # --- Page 4: KPI Reference ---
    pdf.content_page()
    pdf.section_heading('Key Performance Indicators')
    pdf.body(
        'The Control Room tracks the following KPIs to ensure platform health, '
        'research productivity, and infrastructure efficiency:'
    )
    pdf.ln(2)

    pdf.sub_heading('Infrastructure KPIs')
    pdf.bullet('GPU cluster utilisation (target: >90%)')
    pdf.bullet('GPU memory utilisation (target: >80%)')
    pdf.bullet('System uptime (target: 99.95%)')
    pdf.bullet('P99 inference latency (target: <5ms)')
    pdf.bullet('Data pipeline latency (target: <500ms for streaming)')
    pdf.ln(4)

    pdf.sub_heading('Research KPIs')
    pdf.bullet('Active experiments running concurrently')
    pdf.bullet('Experiment completion rate (per week)')
    pdf.bullet('Model validation pass rate')
    pdf.bullet('Simulation throughput (scenarios per hour)')
    pdf.bullet('Data freshness across all asset classes')
    pdf.ln(4)

    pdf.sub_heading('Operational KPIs')
    pdf.bullet('Mean time to detection (MTTD) for incidents')
    pdf.bullet('Mean time to resolution (MTTR)')
    pdf.bullet('Alert noise ratio (actionable vs. false positive)')
    pdf.bullet('Deployment frequency and rollback rate')
    pdf.bullet('Storage growth rate and capacity forecast')
    pdf.ln(6)

    pdf.section_heading('Alert Severity Levels')
    pdf.card_box(
        'P1 - Critical',
        'Complete service outage or data loss. Immediate response required. '
        'Examples: GPU cluster failure, primary data feed loss, storage corruption.',
        15, pdf.get_y(), 85, 35
    )
    pdf.card_box(
        'P2 - High',
        'Degraded performance or partial service impact. Response within 30 min. '
        'Examples: Single node failure, elevated latency, quality score drop.',
        110, pdf.get_y(), 85, 35
    )
    pdf.ln(40)

    pdf.card_box(
        'P3 - Medium',
        'Non-urgent issues with workarounds available. Response within 4 hours. '
        'Examples: Backup delay, non-critical feed gap, capacity warning.',
        15, pdf.get_y(), 85, 35
    )
    pdf.card_box(
        'P4 - Low',
        'Informational alerts and maintenance tasks. Next business day response. '
        'Examples: Certificate renewal, dependency update, cleanup tasks.',
        110, pdf.get_y(), 85, 35
    )
    pdf.ln(38)

    out = os.path.join(OUT_DIR, 'ricche_control_room_dashboard_mockup.pdf')
    pdf.output(out)
    print(f'Control Room Dashboard: {out} ({os.path.getsize(out):,} bytes)')


if __name__ == '__main__':
    generate_architecture_pdf()
    generate_overview_pdf()
    generate_dashboard_pdf()
    print('\nAll PDFs generated successfully.')
