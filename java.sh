set -eou pipefail

javac leetcode.java
java -ea leetcode
rm leetcode.class
