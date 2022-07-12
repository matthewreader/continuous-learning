package leetcode
import org.scalatest.funsuite.AnyFunSuite

class AddTwoIntegersTest extends AnyFunSuite {
  test("case1") {
    assertResult(21)(AddTwoIntegers.sum(10, 11))
  }
}