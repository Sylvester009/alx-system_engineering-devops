#!/usr/bin/env ruby
# regular expression that matches a string that starts with h ends with n
# It can have any single character in between

puts ARGV[0].scan(/h.n/).join
