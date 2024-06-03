import nbformat
from nbconvert import PythonExporter

your_notebook_name ='D:/python_workspace_2024/facenet-pytorch/examples/infer_cn'
# 加载Notebook
with open(your_notebook_name +'.ipynb', 'r', encoding='UTF-8') as f:
    notebook = nbformat.read(f, as_version=4)

# 创建PythonExporter实例
exporter = PythonExporter()

# 转换Notebook
python_script, _ = exporter.from_notebook_node(notebook)

# 保存Python脚本
with open(your_notebook_name +'.py', 'w', encoding='UTF-8') as f:
    f.write(python_script)