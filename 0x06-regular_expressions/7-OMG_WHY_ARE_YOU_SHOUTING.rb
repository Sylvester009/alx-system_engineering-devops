#!/usr/bin/env ruby
# Regular expression that only matches capital letters

puts ARGV[0].scan(/[A-Z]*/).join
