from userge import userge, Message

LOG = userge.getLogger(__name__)

CHANNEL = userge.getCLogger(__name__)

@userge.on_cmd(
    "fw", about={'header': "Global Stable 11.0.1.0 Firmware"})
async def firmware(message: Message):
	LOG.info("Starting fw command...")
    await message.edit('Firmware:\n\nhttps://drive.google.com/file/d/1VFtHwRp6nrHsKFq_tqk9rdmtO-J7NDMB/view?usp=sharing')
	await CHANNEL.log("fw command successfully executed!")
