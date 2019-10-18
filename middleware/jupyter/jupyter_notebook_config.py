import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts
    ipynbが保存されるたびに[py, html, md, tex, pdf]を作成する。"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    base, ext = os.path.splitext(fname)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'markdown', fname], cwd=d)
    # check_call(['jupyter-nbconvert', '--to', 'latex', fname, '--template', 'jsarticle.tplx'], cwd=d)
    # check_call(['extractbb', base+'_files/*.png'], cwd=d)
    # check_call(['platex', '-interaction=nonstopmode', '-synctex=1', '-kanji=utf8', '-guess-input-enc' , base+'.tex'], cwd=d)
    # check_call(['dvipdfmx', base+'.dvi'], cwd=d)

c.FileContentsManager.post_save_hook = post_save
