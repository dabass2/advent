import numpy as np
import scipy.ndimage.filters as filters
import scipy.ndimage.morphology as morphology

def read_file(filename):
  with open(filename, 'r') as f:
    rtn = []
    for line in f.read().splitlines():
      tmp = []
      for digit in list(line):
        tmp.append(int(digit))
      rtn.append(tmp)
    return rtn

def part1():
  arr = np.array(read_file("input.file"))
  local_minima_locations = detect_local_minima(arr)
  print(np.sum(arr[local_minima_locations]+1)-10)

# def part2(input):
#   return

def main():
  print("-----------------")
  print("Running part 1...")
  part1()
  print("-----------------")
#   # print("Running part 2...")
#   # part2()
#   # print("-----------------")

def detect_local_minima(arr):
    # https://stackoverflow.com/questions/3684484/peak-detection-in-a-2d-array/3689710#3689710
    """
    Takes an array and detects the troughs using the local maximum filter.
    Returns a boolean mask of the troughs (i.e. 1 when
    the pixel's value is the neighborhood maximum, 0 otherwise)
    """
    # define an connected neighborhood
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.morphology.html#generate_binary_structure
    neighborhood = morphology.generate_binary_structure(len(arr.shape),2)
    # apply the local minimum filter; all locations of minimum value 
    # in their neighborhood are set to 1
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.filters.html#minimum_filter
    local_min = (filters.minimum_filter(arr, footprint=neighborhood)==arr)
    # local_min is a mask that contains the peaks we are 
    # looking for, but also the background.
    # In order to isolate the peaks we must remove the background from the mask.
    # 
    # we create the mask of the background
    background = (arr==0)
    # 
    # a little technicality: we must erode the background in order to 
    # successfully subtract it from local_min, otherwise a line will 
    # appear along the background border (artifact of the local minimum filter)
    # http://www.scipy.org/doc/api_docs/SciPy.ndimage.morphology.html#binary_erosion
    eroded_background = morphology.binary_erosion(
        background, structure=neighborhood, border_value=1)
    # 
    # we obtain the final mask, containing only peaks, 
    # by removing the background from the local_min mask
    detected_minima = local_min ^ eroded_background
    return np.where(detected_minima)

main()