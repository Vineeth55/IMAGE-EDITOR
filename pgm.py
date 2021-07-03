# name: File path of the pgm image file
# Output is a 2D list of integers
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image

def average(x):
	newimg = []
	H = len(x)
	W = len(x[0])
	newimg = [[0 for i in range(W)] for j in range(H)]
	for i in range(H):
		for j in range(W):
			if i == 0 or i == (H - 1) or j == 0 or j == (W - 1):
				newimg[i][j] = x[i][j]
			else:
				newimg[i][j] = int((x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j]+x[i][j+1]+x[i+1][j-1]+ x[i+1][j]+x[i+1][j+1])/9)
	return newimg
def sqrt(x):
	import math
	return math.sqrt(x)

def access(list,i,j):
	P = len(list)
	Q = len(list[0])
	if i < 0 or i >= P or j < 0 or j >= Q:
		return 0
	else:
		return list[i][j]
def access1(list,i,j):
	P = len(list)
	Q = len(list[0])
	R = []
	for q in range(P):
		R.append(max(list[q]))
	b = max(R)
	if i < 0 or i >= P or j < 0 or j >= Q:
		return b + 1
	else:
		return list[i][j]



def edgedetection(image):
	H = len(image)
	W = len(image[0])
	R = []
	newimg = [[0 for i in range(W)] for i in range(H)] 
	hdif = [[0 for i in range(W)] for i in range(H)]
	vdif = [[0 for i in range(W)] for i in range(H)]
	for i in range(H):
		for j in range(W):
			hdif[i][j] = ((access(image,i-1,j-1)-access(image,i-1,j+1)) + 2*(access(image,i,j-1)-access(image,i,j+1)) + (access(image,i+1,j-1)-access(image,i+1,j+1)))
			vdif[i][j] = ((access(image,i-1,j-1)-access(image,i+1,j-1)) + 2*(access(image,i-1,j)-access(image,i+1,j)) + (access(image,i-1,j+1)-access(image,i+1,j+1)))
			newimg[i][j] = int(sqrt(hdif[i][j]*hdif[i][j] + vdif[i][j]*vdif[i][j]))
	for i in range(H):
		R.append(max(newimg[i]))		
	b = max(R)
	a = 255/b
	for i in range(H):
		for j in range(W):
			newimg[i][j] = int(newimg[i][j]*a)			
	return newimg




		 	




def minenergy(image):
	a = edgedetection(image)
	H = len(a)
	W = len(a[0])
	R = []
	minenergy = [[0 for i in range(W)] for i in range(H)]
	minenergy[0] = a[0]
	for i in range(1,H):
		for j in range(W):
			if j == 0:
				minenergy[i][j] = a[i][j] + min(access(minenergy,i-1,j),access(minenergy,i-1,j+1))
			elif j == W-1:
				minenergy[i][j] = a[i][j] + min(access(minenergy,i-1,j-1),access(minenergy,i-1,j))
			else:
				minenergy[i][j] = a[i][j] + min(access(minenergy,i-1,j-1),access(minenergy,i-1,j),access(minenergy,i-1,j+1))
	for i in range(H):
		R.append(max(minenergy[i]))		
	b = max(R)
	a = 255/b
	for i in range(H):
		for j in range(W):
			minenergy[i][j] = int(minenergy[i][j]*a)
	
	a = minenergy
	b = readpgm('test.pgm')
	i = H-1
	S = []
	for j in range(len(a[H-1])):
		if a[H-1][j] == min(a[H-1]):
			S.append(j)
	for char in S:
		b[H-1][char] = 255
	ct = 0
	while i > 0:
		D = []
		S = list(set(S))
		for char in S:
			m1 = min(access1(a,i-1,char-1),access1(a,i-1,char),access1(a,i-1,char+1))
			for j in range(3):
				if a[i-1][char-1+j] == m1:
					D.append(char-1+j)

		for char in D:
			b[i-1][char] = 255	
		S = D
		i = i - 1
		ct = ct + 1
		print(ct)	
				
	return b

	
# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)

########## Function Calls ##########
x = readpgm('test.pgm')			# test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
y = average(x)
z = edgedetection(x)
b = minenergy(x)
writepgm(y,'average.pgm')
writepgm(z,'edge.pgm')
writepgm(b,'minenergy.pgm')



###################################