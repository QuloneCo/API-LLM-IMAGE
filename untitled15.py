# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u15s-K77LwcV8Ogs9EiKDsUey5oQiGJ2
"""

# Commented out IPython magic to ensure Python compatibility.
#@title Setup
import pkg_resources
print(pkg_resources.get_distribution("torch").version)
from IPython.utils import io
with io.capture_output() as captured:
  !git clone https://github.com/openai/CLIP
  # !pip install taming-transformers
  !git clone https://github.com/CompVis/taming-transformers.git
  !rm -Rf clipit
  !git clone https://github.com/mfrashad/clipit.git
  !pip install ftfy regex tqdm omegaconf pytorch-lightning
  !pip install kornia
  !pip install imageio-ffmpeg
  !pip install einops
  !pip install torch-optimizer
  !pip install easydict
  !pip install braceexpand
  !pip install git+https://github.com/pvigier/perlin-numpy

  # ClipDraw deps
  !pip install svgwrite
  !pip install svgpathtools
  !pip install cssutils
  !pip install numba
  !pip install torch-tools
  !pip install visdom

  !pip install gradio

  !git clone https://github.com/BachiLi/diffvg
#   %cd diffvg
  # !ls
  !git submodule update --init --recursive
  !python setup.py install

# Commented out IPython magic to ensure Python compatibility.
from IPython.utils import io
with io.capture_output() as captured:
  !git clone https://github.com/openai/CLIP
  # !pip install taming-transformers
  !git clone https://github.com/CompVis/taming-transformers.git
  !rm -Rf clipit
  !git clone https://github.com/mfrashad/clipit.git
  !pip install ftfy regex tqdm omegaconf pytorch-lightning
  !pip install kornia
  !pip install imageio-ffmpeg
  !pip install einops
  !pip install torch-optimizer
  !pip install easydict
  !pip install braceexpand
  !pip install git+https://github.com/pvigier/perlin-numpy

  # ClipDraw deps
  !pip install svgwrite
  !pip install svgpathtools
  !pip install cssutils
  !pip install numba
  !pip install torch-tools
  !pip install visdom

  !pip install gradio

  !git clone https://github.com/BachiLi/diffvg
#   %cd diffvg
  # !ls
  !git submodule update --init --recursive
  !python setup.py install
#   %cd ..

  !mkdir -p steps
  !mkdir -p models

# Commented out IPython magic to ensure Python compatibility.
from IPython.utils import io
with io.capture_output() as captured:
  !git clone https://github.com/openai/CLIP
  # !pip install taming-transformers
  !git clone https://github.com/CompVis/taming-transformers.git
  !rm -Rf clipit
  !git clone https://github.com/mfrashad/clipit.git
  !pip install ftfy regex tqdm omegaconf pytorch-lightning
  !pip install kornia
  !pip install imageio-ffmpeg
  !pip install einops
  !pip install torch-optimizer
  !pip install easydict
  !pip install braceexpand
  !pip install git+https://github.com/pvigier/perlin-numpy

  # ClipDraw deps
  !pip install svgwrite
  !pip install svgpathtools
  !pip install cssutils
  !pip install numba
  !pip install torch-tools
  !pip install visdom

  !pip install gradio

  !git clone https://github.com/BachiLi/diffvg
#   %cd diffvg
  # !ls
  !git submodule update --init --recursive
  !python setup.py install
#   %cd ..

  !mkdir -p steps
  !mkdir -p models

pip install moviepy

!pip3 install imageio==2.4.1

!pip install --upgrade imageio-ffmpeg

import sys
sys.path.append("clipit")
import clipit

# To reset settings to default
clipit.reset_settings()

# You can use "|" to separate multiple prompts
prompts = "underwater city"

# You can trade off speed for quality: draft, normal, better, best
quality = "normal"

# Aspect ratio: widescreen, square
aspect = "widescreen"

# Add settings
clipit.add_settings(prompts=prompts, quality=quality, aspect=aspect)

# Apply these settings and run
settings = clipit.apply_settings()
clipit.do_init(settings)
cliptit.do_run(settings)

pip install imageio-ffmpeg