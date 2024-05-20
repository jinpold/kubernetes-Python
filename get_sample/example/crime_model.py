# context, fname, crime, cctv, id, label
from dataclasses import dataclass
import pandas as pd


@dataclass
class CrimeModel:
    _dname : str = ''
    _sname : str = ''
    _fname : str = ''
    _crime : pd.DataFrame = None
    _cctv : pd.DataFrame = None
    
        
    @property
    def dname(self) -> str : return self._dname
    @dname.setter
    def dname(self, dname: str) : self._dname = dname
    @property
    def sname(self) -> str: return self._sname
    @sname.setter
    def sname(self, sname: str): self._sname = sname
    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname: str): self._fname = fname

    @property
    def crime(self) -> pd.DataFrame: return self._crime

    @crime.setter
    def crime(self, crime: pd.DataFrame): self._crime = crime

    @property
    def cctv(self) -> pd.DataFrame: return self._cctv

    @cctv.setter
    def cctv(self, cctv: pd.DataFrame): self._cctv=cctv