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
HIGHLIGHT = (255, 200, 60)    # Gold highlight for key callouts

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
        self.cell(0, 5, 'GPU-Accelerated AI Research Infrastructure for Financial Markets', new_x='LMARGIN', new_y='NEXT')
        # Blue accent line
        self.set_fill_color(*ACCENT)
        self.rect(0, 38, 210, 1.5, 'F')

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', '', 7)
        self.set_text_color(*GRAY)
        self.cell(0, 8, 'Ricche Ltd  |  ricche.ai  |  info@ricche.ai  |  Confidential', align='C')

    def title_page(self):
        self.add_page()
        # Full dark background
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 297, 'F')
        # Accent bar at top
        self.set_fill_color(*ACCENT)
        self.rect(0, 0, 210, 3, 'F')
        self.ln(75)
        self.set_font('Helvetica', 'B', 32)
        self.set_text_color(*WHITE)
        self.cell(0, 16, self.title_text, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(6)
        self.set_font('Helvetica', '', 13)
        self.set_text_color(180, 185, 210)
        self.cell(0, 8, self.subtitle_text, align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(12)
        # Accent rule
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.8)
        self.line(70, self.get_y(), 140, self.get_y())
        self.set_line_width(0.2)
        self.ln(12)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(*ACCENT)
        self.cell(0, 7, 'RICCHE LTD', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(140, 145, 170)
        self.cell(0, 7, 'ricche.ai', align='C', new_x='LMARGIN', new_y='NEXT')
        self.ln(30)
        # Tagline
        self.set_font('Helvetica', '', 9)
        self.set_text_color(100, 105, 130)
        self.cell(0, 6, 'Powered by the NVIDIA Accelerated Computing Stack', align='C', new_x='LMARGIN', new_y='NEXT')

    def content_page(self):
        self.add_page()
        self.dark_header_bar()
        self.set_y(48)

    def ensure_space(self, needed_mm):
        """If less than needed_mm remains on the page, start a new content page."""
        remaining = 297 - self.get_y() - 20  # 297 = A4 height, 20 = bottom margin
        if remaining < needed_mm:
            self.content_page()

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

    def body_bold(self, text):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(*DARK)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def quote_block(self, text):
        """Styled pull-quote / callout."""
        y = self.get_y()
        self.set_fill_color(240, 243, 250)
        self.rect(self.l_margin, y, 180, 18, 'F')
        self.set_fill_color(*ACCENT)
        self.rect(self.l_margin, y, 2, 18, 'F')
        self.set_xy(self.l_margin + 8, y + 3)
        self.set_font('Helvetica', 'BI', 10)
        self.set_text_color(40, 60, 120)
        self.multi_cell(165, 5.5, text)
        self.set_y(y + 22)

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

    def dark_card_box(self, title, body_text, x, y, w=82, h=45):
        """Dark-themed card for high-impact sections."""
        self.set_fill_color(*NAVY)
        self.set_draw_color(40, 50, 80)
        self.rect(x, y, w, h, 'DF')
        self.set_fill_color(*ACCENT)
        self.rect(x, y, w, 1.5, 'F')
        self.set_xy(x + 4, y + 5)
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(*ACCENT)
        self.cell(w - 8, 5, title, new_x='LMARGIN', new_y='NEXT')
        self.set_xy(x + 4, y + 13)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(180, 185, 210)
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
                ax = x + box_w + 1
                ay = y + 7
                self.set_draw_color(*ACCENT)
                self.line(ax, ay, ax + gap - 2, ay)
                self.line(ax + gap - 5, ay - 2, ax + gap - 2, ay)
                self.line(ax + gap - 5, ay + 2, ax + gap - 2, ay)
            x += box_w + gap

    def dark_flow_arrow(self, steps, y):
        """Flow diagram with dark-themed boxes."""
        n = len(steps)
        box_w = 30
        gap = (170 - n * box_w) / max(n - 1, 1)
        x = 20
        for i, step in enumerate(steps):
            self.set_fill_color(30, 35, 55)
            self.set_draw_color(*ACCENT)
            self.rect(x, y, box_w, 14, 'DF')
            self.set_xy(x + 1, y + 2)
            self.set_font('Helvetica', '', 7)
            self.set_text_color(200, 210, 230)
            self.multi_cell(box_w - 2, 3.5, step, align='C')
            if i < n - 1:
                ax = x + box_w + 1
                ay = y + 7
                self.set_draw_color(*ACCENT)
                self.line(ax, ay, ax + gap - 2, ay)
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

    def green_stat_box(self, value, label, x, y, w=40):
        self.set_fill_color(20, 40, 15)
        self.rect(x, y, w, 22, 'F')
        self.set_xy(x, y + 3)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*NVIDIA_GREEN)
        self.cell(w, 7, value, align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_xy(x, y + 12)
        self.set_font('Helvetica', '', 7)
        self.set_text_color(150, 190, 120)
        self.cell(w, 5, label, align='C')

    def cta_block(self, heading, body_text, contact):
        """Call-to-action block at end of document."""
        y = self.get_y() + 4
        self.set_fill_color(*NAVY)
        self.rect(self.l_margin, y, 180, 42, 'F')
        self.set_fill_color(*ACCENT)
        self.rect(self.l_margin, y, 180, 2, 'F')
        self.set_xy(self.l_margin + 8, y + 6)
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(*WHITE)
        self.cell(164, 7, heading, new_x='LMARGIN', new_y='NEXT')
        self.set_xy(self.l_margin + 8, y + 16)
        self.set_font('Helvetica', '', 9)
        self.set_text_color(180, 185, 210)
        self.multi_cell(164, 5, body_text)
        self.set_xy(self.l_margin + 8, y + 32)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(*ACCENT)
        self.cell(164, 6, contact)


# ==============================================================
# PDF 1: Architecture Diagram Pack
# ==============================================================
def generate_architecture_pdf():
    pdf = RicchePDF(
        'Architecture Diagram Pack',
        'Inside the Infrastructure Powering Next-Generation Market Research'
    )
    pdf.title_page()

    # --- Page 2: The Vision ---
    pdf.content_page()
    pdf.section_heading('The Ricche Architecture Vision')
    pdf.body(
        'Financial markets generate more data every day than most industries produce in a year. '
        'Tick-by-tick price movements, shifting order books, macroeconomic releases, satellite '
        'imagery, news sentiment -- the signals are everywhere, but the infrastructure to process '
        'them at scale has traditionally been locked behind the walls of the largest institutions.'
    )
    pdf.body(
        'Ricche is changing that. We are building purpose-built GPU-accelerated research '
        'infrastructure that brings institutional-grade computational power to quantitative '
        'market research. Every layer of our architecture is designed for one goal: turning '
        'raw market complexity into actionable research insights, faster than ever before.'
    )
    pdf.ln(2)
    pdf.quote_block(
        'Our architecture processes 10 billion+ data points through GPU-accelerated pipelines, '
        'delivering 47x faster model training and sub-2ms inference latency.'
    )
    pdf.ln(2)

    # Flow diagram
    pdf.section_heading('End-to-End Platform Architecture')
    pdf.flow_arrow([
        'Market Data\nIngestion',
        'Data\nInfrastructure',
        'ML Research\nEnvironment',
        'Simulation\nFramework',
        'Validation\n& Governance'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.body(
        'Data flows left to right through five purpose-built layers. Each layer is independently '
        'scalable, fault-tolerant, and optimised for its specific workload -- from low-latency '
        'data ingestion to GPU-parallelised model training and real-time inference.'
    )

    pdf.ensure_space(54)
    pdf.card_box(
        'Data Ingestion Layer',
        'Real-time streaming from global exchanges (NYSE, CME, LSE, Eurex, HKEX, SGX). '
        'Tick-level order books, OHLCV pricing, corporate actions, FX rates, and fixed income. '
        'Sub-second ingestion latency with exactly-once delivery guarantees. '
        'Automatic gap detection, reconnection, and data reconciliation.',
        15, pdf.get_y() + 2, 85, 48
    )
    pdf.card_box(
        'GPU Compute & Storage',
        'NVIDIA GPU clusters purpose-built for financial ML workloads. '
        'Distributed columnar storage (Parquet, Arrow) for petabyte-scale datasets. '
        'Smart tiering: hot data on NVMe, warm on SSD, cold on object storage. '
        'Auto-scaling compute allocation with workload-aware scheduling.',
        110, pdf.get_y() + 2, 85, 48
    )
    pdf.ln(54)

    # --- Page 3: GPU Compute -- The Engine ---
    pdf.content_page()
    pdf.section_heading('GPU Compute Infrastructure')
    pdf.body(
        'At the heart of Ricche is a compute layer that would have been unimaginable five years '
        'ago. By building on the full NVIDIA accelerated computing stack, we compress research '
        'cycles from weeks to hours and enable experiments at a scale that was previously the '
        'exclusive domain of billion-dollar hedge funds.'
    )
    pdf.ln(2)

    # NVIDIA tech badges
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
        'Multi-GPU distributed training with mixed-precision (FP16/BF16) delivers dramatic '
        'speedups without sacrificing model quality. Researchers iterate on ideas in hours, '
        'not days. This is the engine that makes everything else possible.',
        15, pdf.get_y(), 85, 52
    )
    pdf.nvidia_card_box(
        'RAPIDS -- Data at GPU Speed',
        'Traditional data pipelines are CPU-bound bottlenecks. RAPIDS cuDF eliminates them '
        'entirely. Feature engineering on financial time-series runs 10-50x faster than pandas. '
        'End-to-end GPU processing means data never leaves the GPU between preparation '
        'and training -- zero transfer overhead, maximum throughput.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    pdf.ensure_space(58)
    pdf.nvidia_card_box(
        'TensorRT -- Production Speed',
        'Research models are optimised for production inference through layer fusion, kernel '
        'auto-tuning, and INT8 quantisation. The result: sub-2ms inference latency for '
        'real-time signal generation. When markets move in milliseconds, every microsecond '
        'of latency reduction translates directly to better research outcomes.',
        15, pdf.get_y(), 85, 52
    )
    pdf.nvidia_card_box(
        'NVIDIA NIM -- Production Deployment',
        'NVIDIA NIM microservices deliver optimised model inference with one-click '
        'deployment and dynamic scaling. Built-in model orchestration handles multi-model '
        'serving with intelligent batching and GPU memory management. '
        'Zero-downtime version transitions with automatic rollback.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    # Performance stats
    pdf.ensure_space(30)
    pdf.green_stat_box('47x', 'GPU vs CPU Training', 15, pdf.get_y(), 42)
    pdf.green_stat_box('<2ms', 'Inference Latency', 62, pdf.get_y(), 42)
    pdf.green_stat_box('10B+', 'Data Points Processed', 109, pdf.get_y(), 42)
    pdf.green_stat_box('50x', 'Feature Eng. Speedup', 156, pdf.get_y(), 38)
    pdf.ln(28)

    # --- Page 4: Data Pipeline ---
    pdf.content_page()
    pdf.section_heading('Data Pipeline Architecture')
    pdf.body(
        'Garbage in, garbage out -- in quantitative research, data quality is everything. '
        'Our multi-stage ingestion pipeline is engineered for institutional-grade reliability, '
        'because the best models in the world are worthless if they are trained on dirty data.'
    )

    pdf.flow_arrow([
        'Exchange\nFeeds',
        'Ingestion\nGateway',
        'Quality\nChecks',
        'Normalisation\n& Alignment',
        'Feature\nStore'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Global Market Coverage')
    pdf.bullet('Equities: Developed and emerging markets across 30+ exchanges worldwide')
    pdf.bullet('Futures & Commodities: Energy, metals, agriculture, financial futures (CME, ICE, LME)')
    pdf.bullet('Options: Full listed chains with Greeks, implied volatility surfaces')
    pdf.bullet('FX: Spot, forwards, crosses -- major and emerging market pairs')
    pdf.bullet('Fixed Income: Government bonds, investment-grade credit, interest rate swaps')
    pdf.bullet('Alternative Data: NLP-processed news, satellite imagery, social sentiment, web scraping')
    pdf.ln(4)

    pdf.ensure_space(48)
    pdf.card_box(
        'Real-Time Streaming',
        'Event-driven pipelines with sub-second latency. Exactly-once delivery semantics '
        'ensure data integrity. Automatic reconnection and gap detection for exchange feeds. '
        'Handles sustained throughput of millions of events per second.',
        15, pdf.get_y(), 85, 42
    )
    pdf.card_box(
        'GPU-Accelerated Batch Processing',
        'Historical backfills and daily reconciliation powered by RAPIDS cuDF. '
        'Idempotent processing with full audit trails and lineage tracking. '
        'Parallel processing across GPU nodes for massive backfill operations. '
        'Data versioning enables reproducible research at any point in time.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(46)

    # --- Page 5: Research Workflow ---
    pdf.content_page()
    pdf.section_heading('Research Workflow -- From Hypothesis to Discovery')
    pdf.body(
        'Great research demands discipline. Every experiment at Ricche follows a structured '
        'workflow designed to eliminate noise, prevent overfitting, and ensure that only '
        'genuinely robust models progress to evaluation. This is not about running more '
        'experiments -- it is about running the right experiments, rigorously.'
    )

    pdf.flow_arrow([
        'Research\nHypothesis',
        'Data\nPreparation',
        'Model\nDevelopment',
        'Simulation\nTesting',
        'Validation\n& Review'
    ], pdf.get_y() + 2)
    pdf.ln(22)

    pdf.sub_heading('Stage 1: Research Hypothesis')
    pdf.body(
        'Every project begins with a clearly defined hypothesis about market behaviour -- '
        'target instruments, timeframes, expected signal characteristics, and falsification '
        'criteria. Hypotheses are registered in our experiment tracking system before any '
        'code is written. This prevents the most dangerous trap in quantitative research: '
        'fitting a narrative to data after the fact.'
    )

    pdf.sub_heading('Stage 2: Data Preparation')
    pdf.body(
        'Relevant datasets are extracted from the feature store with strict temporal discipline '
        '-- no look-ahead bias, ever. GPU-accelerated feature engineering using RAPIDS produces '
        'training-ready datasets 50x faster than traditional tools. Proper train/validation/test '
        'splits with temporal walk-forward design ensure real-world applicability.'
    )

    pdf.sub_heading('Stage 3: Model Development')
    pdf.body(
        'Researchers develop models in CUDA-accelerated PyTorch environments on NVIDIA GPU '
        'clusters. Every hyperparameter, every metric, every model artifact is tracked '
        'automatically. Automated hyperparameter optimisation explores thousands of '
        'configurations. The 47x GPU speedup means researchers test more ideas per week '
        'than traditional setups allow in a month.'
    )

    pdf.sub_heading('Stage 4: Simulation Testing')
    pdf.body(
        'Candidate models face rigorous stress-testing in GPU-parallelised simulation engines. '
        'Monte Carlo simulations evaluate behaviour across 10,000+ market scenarios including '
        'regime changes, liquidity crises, and black swan events. Agent-based simulations '
        'model market microstructure interactions. Only models that survive this gauntlet proceed.'
    )

    pdf.sub_heading('Stage 5: Validation & Peer Review')
    pdf.body(
        'Surviving models undergo out-of-sample validation, walk-forward testing, and formal '
        'peer review. Statistical significance tests (multiple hypothesis correction, bootstrap '
        'confidence intervals) guard against overfitting. Approved models enter controlled '
        'paper-trading evaluation with strict position-size constraints and continuous monitoring.'
    )

    # --- Page 6: Technology Stack ---
    pdf.content_page()
    pdf.section_heading('Technology Stack')
    pdf.body(
        'We chose every tool in our stack for a reason. No resume-driven development, no hype '
        'cycles -- just the best technology for building world-class quantitative research '
        'infrastructure.'
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

    pdf.ln(4)
    pdf.ensure_space(50)
    pdf.cta_block(
        'Build the Future of Market Research With Us',
        'We are looking for partners, collaborators, and visionary researchers who share '
        'our belief that the future of financial markets belongs to those with the best infrastructure.',
        'info@ricche.ai  |  ricche.ai'
    )

    out = os.path.join(OUT_DIR, 'ricche_architecture_diagram_pack.pdf')
    pdf.output(out)
    print(f'Architecture Diagram Pack: {out} ({os.path.getsize(out):,} bytes)')


# ==============================================================
# PDF 2: AI Platform Overview Poster
# ==============================================================
def generate_overview_pdf():
    pdf = RicchePDF(
        'AI Platform Overview',
        'The Infrastructure Redefining Quantitative Market Research'
    )
    pdf.title_page()

    # --- Page 2: Why Ricche Exists ---
    pdf.content_page()
    pdf.section_heading('Why Ricche Exists')
    pdf.body(
        'The quantitative finance landscape is at an inflection point. Traditional approaches '
        '-- hand-crafted models, limited datasets, CPU-bound computation -- are hitting '
        'fundamental limits. The firms that will lead the next decade are those building on '
        'AI-native infrastructure: GPU-accelerated, data-rich, and algorithmically sophisticated.'
    )
    pdf.body(
        'Ricche is building that infrastructure from the ground up. Not by bolting AI onto '
        'legacy systems, but by designing every layer -- from data ingestion to model serving '
        '-- for the scale and speed that modern machine learning demands.'
    )
    pdf.ln(2)
    pdf.quote_block(
        'We believe the next breakthrough in quantitative research will not come from a better '
        'algorithm -- it will come from better infrastructure.'
    )
    pdf.ln(2)

    # Stats row
    pdf.stat_box('47x', 'GPU Acceleration', 15, pdf.get_y(), 42)
    pdf.stat_box('<2ms', 'Inference Latency', 62, pdf.get_y(), 42)
    pdf.stat_box('10B+', 'Data Points', 109, pdf.get_y(), 42)
    pdf.stat_box('24/7', 'Monitoring', 156, pdf.get_y(), 38)
    pdf.ln(30)

    pdf.section_heading('What We Have Built')

    pdf.ensure_space(58)
    pdf.card_box(
        'Machine Learning Research',
        'NVIDIA CUDA-accelerated model training that compresses weeks of experimentation '
        'into hours. PyTorch environments with full experiment tracking, automated '
        'hyperparameter search, and model versioning. Deep learning, gradient boosting, '
        'transformers, and ensemble methods -- all GPU-accelerated.',
        15, pdf.get_y(), 85, 52
    )
    pdf.card_box(
        'Simulation Engines',
        'GPU-parallelised Monte Carlo and agent-based simulations that stress-test '
        'models across 10,000+ market scenarios before they ever see live data. '
        'Regime changes, liquidity shocks, flash crashes -- if a model cannot survive '
        'the simulation gauntlet, it does not progress.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    # --- Page 3: Core Capabilities Continued + NVIDIA ---
    pdf.content_page()

    pdf.card_box(
        'Data Infrastructure',
        'Multi-asset market data spanning equities, futures (including commodities), '
        'options, FX, and fixed income from 30+ global exchanges. Real-time streaming '
        'and historical batch pipelines. GPU-accelerated feature engineering that runs '
        '50x faster than traditional tools. Institutional-grade quality assurance.',
        15, pdf.get_y(), 85, 52
    )
    pdf.card_box(
        'Operations & Monitoring',
        'Real-time Control Room dashboard tracking GPU utilisation, active experiments, '
        'simulation queues, and pipeline throughput. Automated anomaly detection and '
        'alerting. Complete audit trail for every experiment, every model, every '
        'data transformation -- full research governance out of the box.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(58)

    pdf.section_heading('Powered by NVIDIA')
    pdf.body(
        'We built Ricche on the NVIDIA accelerated computing stack because there is no '
        'substitute for raw GPU performance when it comes to financial ML. The numbers speak '
        'for themselves:'
    )
    pdf.ln(2)

    pdf.ensure_space(48)
    pdf.nvidia_card_box(
        'NVIDIA CUDA',
        'The foundation of everything we do. CUDA-accelerated training and simulation '
        'deliver 47x speedups over CPU-only infrastructure. Mixed-precision training '
        '(FP16/BF16) maximises GPU throughput without sacrificing model fidelity.',
        15, pdf.get_y(), 85, 42
    )
    pdf.nvidia_card_box(
        'RAPIDS cuDF',
        'GPU-accelerated DataFrames that make pandas feel like a relic. Feature '
        'engineering on billion-row financial time-series in seconds, not hours. '
        'End-to-end GPU pipelines eliminate the CPU bottleneck entirely.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(46)

    pdf.ensure_space(48)
    pdf.nvidia_card_box(
        'TensorRT',
        'Production inference optimised to sub-2ms latency through layer fusion, '
        'kernel auto-tuning, and INT8 quantisation. When markets move in milliseconds, '
        'this is the difference between leading and lagging.',
        15, pdf.get_y(), 85, 42
    )
    pdf.nvidia_card_box(
        'NVIDIA NIM',
        'Optimised model inference microservices with one-click deployment and dynamic '
        'scaling. Built-in orchestration handles multi-model serving with intelligent '
        'batching. The production layer that scales with our ambition.',
        110, pdf.get_y(), 85, 42
    )
    pdf.ln(46)

    # --- Page 4: Market Coverage + Opportunity ---
    pdf.content_page()
    pdf.section_heading('Global Market Coverage')
    pdf.body(
        'Our data infrastructure spans the world\'s most important financial markets, '
        'with institutional-grade feeds from major exchanges and data providers:'
    )
    pdf.ln(2)
    pdf.bullet('Global Equities -- developed and emerging markets across 30+ exchanges')
    pdf.bullet('Futures & Commodities -- energy, metals, agriculture, financial futures')
    pdf.bullet('Options -- full listed chains with Greeks, volatility surfaces, and skew data')
    pdf.bullet('Foreign Exchange -- spot, forwards, and crosses for major and EM pairs')
    pdf.bullet('Fixed Income -- government bonds, credit markets, and interest rate instruments')
    pdf.bullet('Alternative Data -- NLP-processed news, satellite, sentiment, and web data')
    pdf.ln(6)

    pdf.section_heading('The Opportunity')
    pdf.body(
        'The global quantitative finance market is growing rapidly as AI adoption accelerates '
        'across the financial sector. Traditional quant firms are racing to modernise their '
        'infrastructure. New entrants need institutional-grade tools from day one. The demand '
        'for GPU-accelerated research infrastructure has never been higher.'
    )
    pdf.body(
        'Ricche sits at the intersection of three powerful trends: the explosion of available '
        'market data, the maturation of GPU-accelerated computing, and the proven superiority '
        'of machine learning approaches to financial modelling. We are not building for '
        'today -- we are building for the decade ahead.'
    )
    pdf.ln(4)

    pdf.section_heading('Who Should Partner With Ricche')
    pdf.bullet('Technology providers looking to showcase GPU computing in finance')
    pdf.bullet('Data vendors seeking a showcase platform for their market data products')
    pdf.bullet('Research institutions exploring AI applications in financial markets')
    pdf.bullet('Quantitative firms needing modern, GPU-native research infrastructure')
    pdf.bullet('Investors looking at the convergence of AI, finance, and high-performance computing')
    pdf.ln(6)

    pdf.ensure_space(50)
    pdf.cta_block(
        'Ready to Explore What We Are Building?',
        'Whether you are a potential partner, investor, or researcher, we would love to show you '
        'what GPU-accelerated market research looks like in practice.',
        'info@ricche.ai  |  ricche.ai'
    )

    out = os.path.join(OUT_DIR, 'ricche_ai_platform_overview_poster.pdf')
    pdf.output(out)
    print(f'AI Platform Overview: {out} ({os.path.getsize(out):,} bytes)')


# ==============================================================
# PDF 3: Control Room Dashboard Mockup
# ==============================================================
def generate_dashboard_pdf():
    pdf = RicchePDF(
        'Control Room Dashboard',
        'Real-Time Command and Control for GPU-Accelerated Research Operations'
    )
    pdf.title_page()

    # --- Page 2: Why the Control Room Matters ---
    pdf.content_page()
    pdf.section_heading('The Nerve Centre of Ricche')
    pdf.body(
        'Running GPU-accelerated research infrastructure at scale is like piloting a spacecraft '
        '-- hundreds of systems working in concert, petabytes of data flowing through pipelines, '
        'and millions of computations executing every second. You cannot operate at this scale '
        'without complete, real-time visibility into every layer of the stack.'
    )
    pdf.body(
        'The Ricche Control Room is our answer. A unified operations dashboard that gives '
        'infrastructure operators and research leads a single pane of glass across the entire '
        'platform -- from GPU memory allocation to data pipeline health to experiment progress.'
    )
    pdf.ln(2)

    # Key metrics row
    pdf.stat_box('94.2%', 'GPU Utilisation', 15, pdf.get_y(), 42)
    pdf.stat_box('1,247', 'Active Experiments', 62, pdf.get_y(), 42)
    pdf.stat_box('3.2M', 'Events / sec', 109, pdf.get_y(), 42)
    pdf.stat_box('99.97%', 'Uptime (30d)', 156, pdf.get_y(), 38)
    pdf.ln(30)

    pdf.section_heading('Core Dashboard Panels')

    pdf.ensure_space(64)
    pdf.dark_card_box(
        'GPU Cluster Command',
        'Real-time GPU utilisation heatmap across all nodes. Per-GPU metrics: memory, '
        'temperature, power draw, CUDA kernel throughput. Training job queue with priority '
        'scheduling and estimated completion. Thermal throttling detection and automatic '
        'workload redistribution. GPU failure prediction and proactive alerting.',
        15, pdf.get_y(), 85, 58
    )
    pdf.dark_card_box(
        'Experiment Mission Control',
        'Live tracking of every active ML training experiment. Real-time loss curves, '
        'learning rate schedules, and validation metrics. Per-experiment GPU allocation '
        'and cost tracking. Side-by-side experiment comparison with automated early '
        'stopping recommendations. Historical experiment performance analytics.',
        110, pdf.get_y(), 85, 58
    )
    pdf.ln(62)

    pdf.ensure_space(58)
    pdf.dark_card_box(
        'Data Pipeline Operations',
        'Feed-by-feed ingestion dashboard with per-exchange latency and throughput. '
        'Real-time data quality scoring with drift detection. Automatic gap detection '
        'and backfill orchestration. End-to-end pipeline lineage -- trace any feature '
        'back to its raw data source. Multi-region feed redundancy status.',
        15, pdf.get_y(), 85, 52
    )
    pdf.dark_card_box(
        'Simulation War Room',
        'Live Monte Carlo and agent-based simulation monitoring. Queue depth, GPU '
        'allocation, and estimated runtimes per simulation batch. Result visualisation '
        'with scenario coverage heatmaps. Pass/fail indicators with statistical '
        'confidence levels. Scenario stress-test coverage analysis.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    # --- Page 3: Infrastructure Monitoring ---
    pdf.content_page()
    pdf.section_heading('Infrastructure Intelligence')
    pdf.body(
        'Modern research infrastructure is too complex for reactive monitoring. The Control '
        'Room uses predictive analytics to anticipate problems before they impact research '
        'workflows -- because a GPU failure during a 12-hour training run is not just an '
        'incident, it is lost research time that can never be recovered.'
    )
    pdf.ln(2)

    pdf.ensure_space(60)
    pdf.dark_card_box(
        'Compute Resource Orchestration',
        'Kubernetes cluster overview with real-time pod scheduling and resource allocation. '
        'GPU scheduling queue with multi-tier priority (research, simulation, inference). '
        'Predictive auto-scaling based on historical workload patterns. Capacity forecasting '
        'with 7-day and 30-day projections. Cost optimisation recommendations.',
        15, pdf.get_y(), 85, 55
    )
    pdf.dark_card_box(
        'Storage & Network Intelligence',
        'Distributed storage heatmap: NVMe (hot), SSD (warm), object storage (cold). '
        'Automatic data lifecycle management and tier migration. Network throughput '
        'between compute and storage with congestion detection. I/O latency tracking '
        '(p50, p95, p99). Predictive capacity alerts before you run out.',
        110, pdf.get_y(), 85, 55
    )
    pdf.ln(60)

    pdf.ensure_space(58)
    pdf.dark_card_box(
        'Model Serving Dashboard (NIM)',
        'NVIDIA NIM microservice metrics: RPS, latency distributions, batch '
        'utilisation, and GPU memory per model. Live A/B test traffic routing. Model '
        'version deployment history with one-click rollback. SLA compliance tracking '
        'with automatic alerting when latency targets are breached.',
        15, pdf.get_y(), 85, 52
    )
    pdf.dark_card_box(
        'Incident Command Centre',
        'Active alert dashboard with intelligent severity classification (P1-P4). '
        'Automated root cause analysis using infrastructure graph correlation. Mean '
        'time to detection (MTTD) and resolution (MTTR) trending. On-call routing '
        'with escalation workflows. Post-incident review automation.',
        110, pdf.get_y(), 85, 52
    )
    pdf.ln(56)

    # --- Page 4: KPIs & Operational Excellence ---
    pdf.content_page()
    pdf.section_heading('Operational Excellence Metrics')
    pdf.body(
        'What gets measured gets improved. The Control Room tracks a comprehensive set '
        'of KPIs designed to maximise research throughput while maintaining infrastructure '
        'reliability. These are not vanity metrics -- each one directly impacts our ability '
        'to produce better research, faster.'
    )
    pdf.ln(2)

    pdf.sub_heading('Infrastructure Performance')
    pdf.bullet('GPU cluster utilisation: >90% target (currently 94.2%)')
    pdf.bullet('GPU memory efficiency: >80% target with smart workload packing')
    pdf.bullet('Platform uptime: 99.95% SLA (currently 99.97% over 30 days)')
    pdf.bullet('P99 inference latency: <5ms target (currently <2ms via TensorRT)')
    pdf.bullet('Data pipeline end-to-end latency: <500ms for streaming feeds')
    pdf.ln(4)

    pdf.sub_heading('Research Productivity')
    pdf.bullet('Concurrent experiments: 1,200+ active at peak')
    pdf.bullet('Experiment iteration speed: 47x faster than CPU-only infrastructure')
    pdf.bullet('Model validation throughput: 10,000+ simulation scenarios per candidate')
    pdf.bullet('Feature engineering pipeline speed: 50x faster via RAPIDS GPU processing')
    pdf.bullet('Researcher time-to-first-experiment: <30 minutes for new projects')
    pdf.ln(4)

    pdf.sub_heading('Operational Reliability')
    pdf.bullet('Mean time to detection (MTTD): <2 minutes for P1 incidents')
    pdf.bullet('Mean time to resolution (MTTR): <15 minutes for infrastructure issues')
    pdf.bullet('Alert signal-to-noise ratio: >85% actionable (minimise fatigue)')
    pdf.bullet('Deployment frequency: multiple per day with zero-downtime GitOps')
    pdf.bullet('Data quality score: >99.5% across all asset classes')
    pdf.ln(6)

    pdf.section_heading('Alert Classification')
    pdf.ensure_space(38)
    pdf.card_box(
        'P1 -- Critical (Immediate)',
        'GPU cluster failure, primary data feed outage, storage corruption, or complete '
        'service unavailability. War room activated. All hands on deck.',
        15, pdf.get_y(), 85, 32
    )
    pdf.card_box(
        'P2 -- High (30 min)',
        'Degraded GPU performance, partial feed disruption, elevated latency, or data '
        'quality score drop. On-call engineer engaged with escalation path.',
        110, pdf.get_y(), 85, 32
    )
    pdf.ln(36)

    pdf.ensure_space(38)
    pdf.card_box(
        'P3 -- Medium (4 hours)',
        'Non-critical feed gap, backup delay, capacity warning, or non-production '
        'component degradation. Tracked and scheduled for resolution.',
        15, pdf.get_y(), 85, 32
    )
    pdf.card_box(
        'P4 -- Low (Next day)',
        'Informational: certificate renewals, dependency updates, cleanup tasks, '
        'and capacity planning triggers. Queued for routine maintenance.',
        110, pdf.get_y(), 85, 32
    )
    pdf.ln(38)

    pdf.ensure_space(50)
    pdf.cta_block(
        'See the Control Room in Action',
        'We would love to walk you through a live demo of the Control Room and show you '
        'what real-time GPU infrastructure management looks like at scale.',
        'info@ricche.ai  |  ricche.ai'
    )

    out = os.path.join(OUT_DIR, 'ricche_control_room_dashboard_mockup.pdf')
    pdf.output(out)
    print(f'Control Room Dashboard: {out} ({os.path.getsize(out):,} bytes)')


if __name__ == '__main__':
    generate_architecture_pdf()
    generate_overview_pdf()
    generate_dashboard_pdf()
    print('\nAll PDFs generated successfully.')
