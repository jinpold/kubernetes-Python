from dataclasses import dataclass
import pandas as pd


@dataclass
class DataSets:
    _context: str = ""
    _fname: str = ''    # file name
    _dname: str = ''    # data name
    _sname: str = ''    # save path
    _train: pd.DataFrame = None
    _test: pd.DataFrame = None
    _id: pd.DataFrame = None
    _label: pd.DataFrame = None

    @property
    def context(self) -> str:    return self.__context

    @context.setter
    def context(self, context:str): self.__context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname:str): self._fname = fname

    @property
    def dname(self) -> str: return self._dname

    @fname.setter
    def dname(self, dname:str): self._dname = dname

    @property
    def sname(self) -> str: return self._sname

    @fname.setter
    def sname(self, sname:str): self._sname = sname
   
    @property
    def train(self) -> pd.DataFrame: return self._train
   
    @train.setter
    def train(self, train:pd.DataFrame): self._train = train
   
    @property
    def test(self) -> pd.DataFrame: return self._test
   
    @test.setter
    def test(self, test:pd.DataFrame): self._test = test
   
    @property
    def id(self) -> pd.DataFrame: return self._id
   
    @id.setter
    def id(self, id:pd.DataFrame): self._id = id
   
    @property
    def label(self) -> pd.DataFrame: return self._label
   
    @label.setter
    def label(self, label:pd.DataFrame): self._label = label