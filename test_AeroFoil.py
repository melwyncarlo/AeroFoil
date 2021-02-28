import subprocess

def test_main():
	test_proc = subprocess.call(['sh', 'if freecad AeroFoil.FCMacro & then echo "True"; kill $!; else echo "False"; fi'])

