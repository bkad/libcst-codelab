import libcst as cst
import libcst.matchers as m
from libcst.codemod import VisitorBasedCodemodCommand


class Optional(VisitorBasedCodemodCommand):
    DESCRIPTION = "Refactors uses of Optional[x] into x | None."
