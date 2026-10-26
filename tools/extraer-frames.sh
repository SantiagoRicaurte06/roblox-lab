#!/bin/bash
# Uso: ./tools/extraer-frames.sh video.mp4 nombre 2   (1 frame cada 2 seg)
ffmpeg -i "$1" -vf "fps=1/${3:-2}" "referencias/videos/frames/${2}_%04d.png"
