#!/usr/bin/env ruby
# Ruby script thats output: [SENDER],[RECEIVER],[FLAGS]

sender = ARGV[0].scan(/from:(.*?)\]/)
receiver = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [sender, receiver, flags].join(",")
