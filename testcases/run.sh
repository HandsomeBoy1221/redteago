cd ..
rm -rf result
mkdir result
cd testcases/
pytest test_runall.py --alluredir=../result