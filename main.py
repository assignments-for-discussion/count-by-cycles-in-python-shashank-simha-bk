
def count_batteries_by_usage(cycles):
    lowCount= 0,
    mediumCount= 0,
    highCount= 0
    return {
    if cycles<150:
      lowCount=lowCount+1;
      print('The charge cycle is low and the low count cycle is ' +lowCount)
    elif cycles>150 or cycles<650:
      mediumCount=mediumCount+1;
      print('The charge cycle is medium and the medium count cycle is ' +mediumCount)
    else cycles>650:
      highCount=highCount+1;
      print('The charge cycle is high and the high count cycle is ' +highCount)
  
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  # assert(counts["lowCount"] == 1)
 # assert(counts["mediumCount"] == 3)
  #assert(counts["highCount"] == 2)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
