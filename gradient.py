import numpy as np

MIN_SIZE = 3


def check_rect(arr, x, y):
  val = arr[x][y]
  step = 1
  len = 0
  if arr[x][y+1] != val:
    for j in range(y+1, arr.shape[1]):
      if arr[x][j] == 0:
        step += 1
      else:
        break
  for j in range(y, arr.shape[1]):
    if ((j-y) % step) == 0 and arr[x][j] != val:
      break
    if ((j-y) % step) != 0 and arr[x][j] != 0:
      break
    if ((j-y+1) % step) == 0:
      len += 1
  leny = len*step
  lenx = 1
  for i in range(x+1, arr.shape[0]):
    if (arr[x][y:y+leny] != arr[i][y:y+leny]).any():
      break
    lenx += 1
  return (lenx, leny)


def is_in_rects(rects, i, j):
  for rect in rects:
    if i >= rect[0][0] and i < rect[0][0] + rect[1][0] and j >= rect[0][1] and i < rect[0][1] + rect[1][1]:
      return True
  return False


def get_rects(arr):
  rects = []
  for i in range(arr.shape[0]-MIN_SIZE+1):
    for j in range(arr.shape[1]-MIN_SIZE+1):
      if not is_in_rects(rects, i, j):
        size = check_rect(arr, i, j)
        if size[0] >= MIN_SIZE and size[1] >= MIN_SIZE:
          rects.append([(i, j), size])
  return rects


def get_xrects(arr, rects):
  res_rects = []
  for rect in rects:
    mat = arr[rect[0][0]:rect[0][0]+rect[1][0], rect[0][1]:rect[0][1]+rect[1][1]]
    mat_rects = get_rects(mat.T)
    for mrect in mat_rects:
      mrect[0] = (rect[0][0] + mrect[0][1] - 1, rect[0][1] + mrect[0][0] - 1)
      mrect[1] = (mrect[1][1], mrect[1][0])
    print(mat_rects)


def get_gradient(arr):
  xdiff = np.diff(arr, axis=0)
  xdiff = np.pad(xdiff, [(1, 0), (0, 0)], mode='constant')
  
  ydiff = np.diff(arr, axis=1)
  ydiff = np.pad(ydiff, [(0, 0), (1, 0)], mode='constant')

  rects = get_rects(ydiff)
  rects = get_xrects(xdiff, rects)
  return rects




array = np.array([
          [1, 0, 1, 1, 0, 1, 2], 
          [1, 1, 1, 2, 3, 4, 2], 
          [1, 6, 2, 3, 4, 5, 2], 
          [1, 1, 3, 4, 5, 6, 2], 
          [1, 1, 4, 5, 6, 7, 2]])

get_gradient(array)

