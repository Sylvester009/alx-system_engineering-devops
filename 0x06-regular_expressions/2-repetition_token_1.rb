#!/usr/bin/env ruby
# a Ruby script that accepts one argument and pass it to a regular expression.
# to match htn, hbtn

puts ARGV[0].scan(/hb?tn/).join
