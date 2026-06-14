from nmk_base._buildenv.template import NmkBaseProjectTemplate, NmkReference


class NmkWorkspaceProjectTemplate(NmkBaseProjectTemplate):
    """
    Template for **nmk-workspace** plugin project
    """

    @property
    def weight(self) -> int:
        # Top level plugin weight
        return 400

    @property
    def auto_extra(self) -> bool:
        # Default extra
        return True

    @property
    def references(self) -> list[NmkReference]:
        return super().references + [NmkReference("nmk-workspace!plugin.yml", ["nmk-base!plugin.yml"])]

    @property
    def description(self) -> str:
        return "workspace nmk project"
