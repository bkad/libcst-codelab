import libcst as cst
import libcst.matchers as m
from libcst.codemod import VisitorBasedCodemodCommand


class Optional(VisitorBasedCodemodCommand):
    DESCRIPTION = "Refactors uses of Optional[x] into x | None."

    def leave_Subscript(
        self, original_node: cst.Subscript, updated_node: cst.Subscript
    ) -> cst.BaseExpression:
        if m.matches(updated_node, m.Subscript(value=m.Name("Optional"))):
            return cst.BinaryOperation(
                left=updated_node.slice[0].slice.value,
                operator=cst.BitOr(),
                right=cst.Name(value="None"),
            )
        return updated_node
