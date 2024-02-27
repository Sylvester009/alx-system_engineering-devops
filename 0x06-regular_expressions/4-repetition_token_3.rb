#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it to a regular expression
# regex should not contain square brackets
# TO match "hbn, hbtn, hbtttttn" not "hbon"

puts ARGV[0].scan(/hbt*n/).join
