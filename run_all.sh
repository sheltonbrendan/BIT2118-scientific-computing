#!/usr/bin/env bash
# Runs every program from the repo root; figures are saved to outputs/figures, text to outputs/
mkdir -p outputs/figures /tmp/run
for f in code/Task_*.py code/extensions/Task_*.py; do
  [ -f "$f" ] || continue
  n=$(basename "$f" .py); t=${n:0:7}
  sed "s#plt.show()#plt.savefig('outputs/figures/${n}.png', dpi=150); plt.close()#" "$f" > /tmp/run/$n.py
  MPLBACKEND=Agg python3 /tmp/run/$n.py > outputs/${n}_output.txt 2>&1 || echo "FAIL $n"
done
