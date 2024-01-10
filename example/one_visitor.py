import libcst as cst
import libcst.matchers as m
from libcst.codemod import VisitorBasedCodemodCommand


class OneVisitor(VisitorBasedCodemodCommand):
    DESCRIPTION = "Refactors uses of '1' to '9'"

    def leave_Integer(
        self, original_node: cst.Integer, updated_node: cst.Integer
    ) -> cst.BaseExpression:
        if m.matches(updated_node, m.Integer(value="1")):
            return cst.Integer(value="9")
        return updated_node
