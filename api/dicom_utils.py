import datetime
import pydicom
from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import generate_uid
import numpy as np

def to_dicom(img: np.ndarray, path="output.dcm"):
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = generate_uid()
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.ImplementationClassUID = generate_uid()

    ds = FileDataset(path, {}, file_meta=file_meta, preamble=b"\0" * 128)
    # Minimal clinical-style metadata (extend as needed)
    ds.PatientName = "Synthetic^Patient"
    ds.PatientID = "SYN001"
    ds.Modality = "OT"
    ds.StudyInstanceUID = generate_uid()
    ds.SeriesInstanceUID = generate_uid()
    ds.SOPInstanceUID = generate_uid()
    ds.StudyDate = datetime.datetime.now().strftime("%Y%m%d")
    ds.StudyTime = datetime.datetime.now().strftime("%H%M%S")

    ds.Rows, ds.Columns = img.shape
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.BitsAllocated = 8
    ds.BitsStored = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = img.tobytes()
    ds.save_as(path)
    return path
