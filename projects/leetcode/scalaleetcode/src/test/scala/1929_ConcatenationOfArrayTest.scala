package leetcode.scalaleetcode
import org.scalatest.funsuite.AnyFunSuite

class ConcatenationOfArrayTest extends AnyFunSuite {
  test("ConcatenationOfArray.getConcatenation") {
    assert(ConcatenationOfArray.getConcatenation(Array(1,2,3)) === Array(1,2,3,1,2,3))
    assert(ConcatenationOfArray.getConcatenation(Array(1)) === Array(1,1))
  }
}
