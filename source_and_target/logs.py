import logging

logging.basicConfig(
    filename='./a.log',   # ✅ correct argument name
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logs = logging.getLogger('./orchestrations.py/')

