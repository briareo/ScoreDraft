from . import PyScoreDraft

def ObjectToId(obj):
	'''
	Utility only used intenally. User don't use it.
	'''
	if type(obj) is list:
		return [ObjectToId(sub_obj) for sub_obj in obj]
	else:
		return obj.id

defaultNumOfChannels=2
def setDefaultNumberOfChannels(defChn):
	if defChn<1:
		defChn=1
	elif defChn>2:
		defChn=2
	global defaultNumOfChannels
	defaultNumOfChannels=defChn

class TrackBuffer:
	'''
	Basic data structure storing waveform.
	The content can either be generated by "play" and "sing" calls or by mixing track-buffer into a new one
	'''
	def __init__ (self, chn=-1):
		'''
		chn is the number of channels, which can be 1 or 2
		'''
		if chn==-1:
			chn=defaultNumOfChannels
		if chn<1:
			chn=1
		elif chn>2:
			chn=2
		self.id= PyScoreDraft.InitTrackBuffer(chn)

	def __del__(self):
		PyScoreDraft.DelTrackBuffer(self.id)

	def setVolume(self,volume):
		'''
		Set the volume of the track. This value is used as a weight when mixing tracks.
		volume -- a float value, in range [0.0,1.0]
		'''
		PyScoreDraft.TrackBufferSetVolume(self.id, volume)

	def getVolume(self):
		'''
		Get the volume of the track. This value is used as a weight when mixing tracks.
		Returned value is a float
		'''
		return PyScoreDraft.TrackBufferGetVolume(self.id)

	def setPan(self, pan):
		'''
		Set the panning of the track. This value is used when mixing tracks.
		pan -- a float value, in range [-1.0,1.0]
		'''
		PyScoreDraft.TrackBufferSetPan(self.id, pan)

	def getPan(self):
		'''
		Get the panning of the track. This value is used when mixing tracks.
		Returned value is a float
		'''
		return PyScoreDraft.TrackBufferGetPan(self.id)

	def getNumberOfSamples(self):
		'''
		Get the number of PCM samples of the buffer.
		Returned value is an integer
		'''
		return PyScoreDraft.TrackBufferGetNumberOfSamples(self.id)

	def getNumberOfChannles(self):
		'''
		Get the number of Channels of the buffer.
		Returned value is an integer
		'''
		return PyScoreDraft.TrackBufferGetNumberOfChannels(self.id)

	def getCursor(self):
		'''
		Get the cursor position of the buffer.
		The unit is in number of samples.
		Returned value is a float
		'''
		return PyScoreDraft.TrackBufferGetCursor(self.id)

	def setCursor(self, cursor):
		'''
		Set the curosr position of the buffer.
		The unit is in number of samples.
		cursor -- a float value, cursor >= 0.0
		'''
		PyScoreDraft.TrackBufferSetCursor(self.id, cursor)

	def moveCursor(self, cursor_delta):
		'''
		Set the curosr position of the buffer to current position + cursor_delta.
		The unit is in number of samples.
		cursor_delta -- a float value
		'''
		PyScoreDraft.TrackBufferMoveCursor(self.id, cursor_delta)


def MixTrackBufferList (targetbuf, bufferList):
	'''
	Function used to mix a list of track-buffers into another one
	targetbuf -- an instance of TrackBuffer to contain the result
	bufferList -- a list a track-buffers
	'''
	PyScoreDraft.MixTrackBufferList(targetbuf.id, ObjectToId(bufferList))

def WriteTrackBufferToWav(buf, filename):
	'''
	Function used to write a track-buffer to a .wav file.
	buf -- an instance of TrackBuffer
	filename -- a string
	'''
	PyScoreDraft.WriteTrackBufferToWav(buf.id, filename)

def ReadTrackBufferFromWav(buf, filename):
	'''
	Function used to read a track-buffer from a .wav file.
	buf -- an instance of TrackBuffer
	filename -- a string
	'''
	PyScoreDraft.ReadTrackBufferFromWav(buf.id, filename)

