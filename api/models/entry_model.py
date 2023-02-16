from pydantic import BaseModel

class Entry(BaseModel):
    entry_id: int
    address: str
    reasons: list[str]
    needs: list[str]

    def __str__(self):

        reasons_text = ""
        for reason in self.reasons:
            reasons_text += reason + " "

        needs_text = ""
        for need in self.needs:
            needs_text += need + " "

        return self.address + "reason: " + reasons_text + "needs: " + needs_text
