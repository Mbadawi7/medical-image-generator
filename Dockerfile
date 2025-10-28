# ============================================
# Dockerfile for AI Medical Image Generator
# Optimized for Apple Silicon / macOS ARM64
# ============================================

FROM python:3.14-slim

ENV DEBIAN_FRONTEND=noninteractive

# ------------------------------------------------
# Install base system dependencies and build tools
# ------------------------------------------------


RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    gcc \
    g++ \
    clang \
    pkg-config \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libopenblas-dev \
    libc-dev \
    ninja-build \
    meson \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
# ------------------------------------------------
# Copy requirements into container
# ------------------------------------------------
COPY requirements.txt /tmp/

# ------------------------------------------------
# Upgrade pip & core build tools
# ------------------------------------------------
RUN pip install --upgrade pip setuptools wheel cmake

# ------------------------------------------------
# Install Python dependencies (strict)
# ------------------------------------------------
# Disable stringzilla SIMD/SVE build (breaks on ARM Mac)
ENV CFLAGS="-DSTRINGZILLA_DISABLE_SVE=1"

# Clean pip cache to prevent broken wheels from reusing
RUN pip cache purge || true

# Install Python dependencies (strict but ARM-safe)
RUN pip install -r /tmp/requirements.txt --no-cache-dir --prefer-binary

# ------------------------------------------------
# Install PyTorch (ARM CPU/MPS compatible)
# ------------------------------------------------
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# ------------------------------------------------
# Set up workspace & expose JupyterLab port
# ------------------------------------------------
WORKDIR /workspace
EXPOSE 8888

# ------------------------------------------------
# Default command: start JupyterLab automatically
# ------------------------------------------------
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token="]

