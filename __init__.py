import io
import os.path
import subprocess

from list_all_files_recursively import get_folder_file_complete_path
from getfilenuitkapython import get_filepath
import pandas as pd
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions

pd_add_apply_ignore_exceptions()
from a_pandas_ex_less_memory_more_speed import pd_add_less_memory_more_speed

pd_add_less_memory_more_speed()
sigcheck = get_filepath("sigcheck.exe")

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = subprocess.CREATE_NO_WINDOW
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
    "start_new_session": True,
}


def get_sig_infos(
    path: str | tuple | list, extensions: tuple | list = ()
) -> pd.DataFrame:
    r"""
    The get_sig_infos function is used to retrieve signature information for files located at a given path or paths
    using the sigcheck.exe utility.
    It collects information such as file signatures, file version, description, and other relevant details.

    This function might be interesting for individuals or developers working with files and file security analysis.
    It can be particularly useful for tasks like identifying the digital signatures of executable files, verifying file
    authenticity, checking for file tampering, and gathering metadata about files in a specified location.

    Advantages of the get_sig_infos function include:

    Automation:
    The function automates the process of retrieving signature information for multiple files or folders,
    saving time and effort compared to manually analyzing each file.

    Extensibility:
    It allows users to specify the path(s) and file extensions to analyze,
    making it flexible and adaptable to different scenarios and requirements.

    Integration with Pandas:
    The function leverages Pandas to organize the collected information into a DataFrame,
    enabling further data manipulation, analysis, and integration with other data processing workflows.

    Error Handling:
    The function includes error handling mechanisms, such as ignoring exceptions during
    the signature analysis and printing any encountered exceptions for debugging purposes.
    This helps ensure that the function can handle a variety of scenarios and continue processing
    files even if some exceptions occur.

    Performance Optimization:
    The function applies performance optimization techniques, such as reducing memory usage
    and using efficient Pandas operations,
    to enhance the efficiency and speed of the signature analysis process.

        Retrieves signature information for files located at the given path(s) using the sigcheck.exe utility.

        Args:
            path (str|tuple|list): Path(s) to the file(s) or folder(s) to analyze. It can be a single path as a string,
                a tuple of paths, or a list of paths.
            extensions (tuple|list, optional): File extensions to consider. Only files with these extensions will be analyzed.
                Defaults to (".exe", ".cmd").

        Returns:
            pd.DataFrame: A Pandas DataFrame containing the signature information for the analyzed files.


            df = get_sig_infos(path=r"C:\Program Files (x86)\BlueStacks X", extensions=())
        print(df[:10].to_string())
                                                                                Path Verified                Date               Publisher                Company      Description                             Product   Product Version                            File Version Machine Type    Binary Version Original Name Internal Name                                     Copyright Comments  Entropy                               MD5                                      SHA1                                    PESHA1                                                          PESHA256                                                            SHA256                               IMP
    0                                     c:\program files (x86)\bluestacks x\7z.dll   Signed 2021-10-29 00:26:00  Bluestack Systems, Inc            Igor Pavlov        7z Plugin                               7-Zip              19.0                                    19.0       32-bit          19.0.0.0        7z.dll            7z           Copyright (c) 1999-2018 Igor Pavlov      NaN    6.623  544076DED188D227DBC7DC3C5D72762A  381A09F5D0B1C49492DA8EA91D5A5A9C08635534  8012FB95899DC92D049773F6B21DC776D7F6ACB7  4EBD65A45F27AD6CA66FD3969F883578530062E0A751C4F55E6CD1AC9AEE2E1B  721879078AFAC97327471023FC774C54F3248F47A1383A71EF61AC0DB470894B  622EAE4411B119BF4CA7BEE4FA1391C8
    1                                     c:\program files (x86)\bluestacks x\7z.exe   Signed 2021-10-29 00:26:00  Bluestack Systems, Inc            Igor Pavlov    7-Zip Console                               7-Zip              19.0                                    19.0       32-bit          19.0.0.0        7z.exe            7z           Copyright (c) 1999-2018 Igor Pavlov      NaN    6.603  DC1882CBD821506758F6C689C796BF3E  E8C6C24CC0FF9A402ED51CC1756DC3A1A0F1EE49  D0EE4A7BD32FE712448785B1F5BC74E9305D1327  49E102C046CDF5E2375B60B9CF88806757FD0B13B99843E6E99E5D907EA2208B  9AD95EC3A25E89E19FA9AF5B254FECD8EF129D3C412B9A805B6911BB2D031FFD  C2674610547987E150CA76C2C9C784A0
    2            c:\program files (x86)\bluestacks x\api-ms-win-core-file-l1-2-0.dll   Signed 2015-07-14 23:55:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.622  04C39B760247C6EED86854F657833347  9490B9DCD3F91B06FA7F3028DC5DF5B4A22D4FBC  7D3B10BA52968F88451AA8368FEC6B798BBBCB28  D296400340B5E1102E1DF12B1F997D408A9A5A184E88AFA4D4C9A6EEF0114EA6  F56B749C01CC82118FFE538674DF22A1F4EF7A07E94E559D25F55CE104E7B095                              <NA>
    3            c:\program files (x86)\bluestacks x\api-ms-win-core-file-l2-1-0.dll   Signed 2015-07-14 23:55:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.733  8403E7B9EC4B0C4F6C9BF0EC93687C77  7581E7D872EC9C00F33BDAC9690E55096DB30172  90164EB28E0BE20C677D4C6BCA2F271CD75A31AE  3A5CAED01B3F498DC111365327A81D9787964CA19DB9D11102FD8A62B91E846C  A8B79E230A81102735996500DD00D34BFA77955C11D87C0F9C967EC85003E116                              <NA>
    4    c:\program files (x86)\bluestacks x\api-ms-win-core-localization-l1-2-0.dll   Signed 2015-07-14 23:56:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.666  2E2C78125C66CDE5859559F5E6167034  F00E9CDD8DA93106FB3BC060E64C643E2274A598  901F6DD87F70D2B89B59F9C6E1C09BB927CABFB6  1EC4863EEF89E9CA9B165FA9A25BA5914B8FCA2D5FCCAF041E9D798F37C5D0CE  9BF2BFF3ADCB1FB5707794B18320D7113F45446DD505EEE43ABBF8835CD73A44                              <NA>
    5  c:\program files (x86)\bluestacks x\api-ms-win-core-processthreads-l1-1-1.dll   Signed 2015-07-14 23:56:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.653  5EFD5F4B617E95043898DBFD78AF97FB  70BABD7098B05C59484A9DBEA77F4B5DCD2BF9CC  89263725D098FC15982C1636591180461B38593C  961C541A92C71ED5BD0E7B3C56F2CAEE6F753B0654A530B89C1F28B9B81C165A  CFCEFC5AF3F7A37242DCDBFEBEDBB954A0D21D93175441BCE680A1A4C1C9FEF3                              <NA>
    6           c:\program files (x86)\bluestacks x\api-ms-win-core-synch-l1-2-0.dll   Signed 2015-07-14 23:55:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.701  FD9C6D2E90B3CF9C0D72F59B66EA1989  92BE1C1C7BC81E2EAEB22FDCE5946A0FB08E45F2  010F285E42AB1F9496EC17A087F2E4B9FFA53A76  C994FAF1B8D8B2983C7374BA2D9845BADED8F766F8675E6BE9A571A8EE2F81E3  05482DBB67F005E0B61BBD44CE04818254FFECB765F836324BBCB3DD174524FE                              <NA>
    7        c:\program files (x86)\bluestacks x\api-ms-win-core-timezone-l1-1-0.dll   Signed 2015-07-14 23:55:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.745  425083789D9D675B2BCFA9A603C9B3FA  C6E4BCA5924406A675686B30EF5708732667E079  2B774BD436108E17877413A6C23DBA94BF23CDB8  049F29B7658A9E3B242F6180EF95C4AF92BF5B07086FEBD20DD06978903ACFC5  0006C449FDED67CB7CD9DFB4FA9310CE5103CA3B1344AF72052509C8B1CD4AD2                              <NA>
    8          c:\program files (x86)\bluestacks x\api-ms-win-core-xstate-l2-1-0.dll   Signed 2015-07-14 23:56:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.649  2668196CED304462699D69EE80C19DFC  726F61F3F20528AF09DB801EF895AC11B228FA94  9DE1354ED86824686CF219F8B5F55367DBED011A  BA9809B79ED5D3C610EB46680E2B3E82F735086880FFE0C5D878DCAE04B94D60  B1ED09F172A43A826853DE69851B8F2ABCB80577D67BD9755C45FAFC8199A2C9                              <NA>
    9            c:\program files (x86)\bluestacks x\api-ms-win-crt-conio-l1-1-0.dll   Signed 2015-07-14 23:55:00       Microsoft Windows  Microsoft Corporation  ApiSet Stub DLL  Microsoft Windows Operating System  10.0.10240.16390  10.0.10240.16390 (th1_st1.150714-1601)       32-bit  10.0.10240.16390    apisetstub    apisetstub   Microsoft Corporation. All rights reserved.      NaN    6.626  8E534F49C77D787DB69BABFF931A497A  709380F53F4BEE25AD110869AC4E755391346405  F096EB68F5AF471D47CAEE160887C72E2BE9A9FF  36742CF2B4E66FCFF31D6CDCE23C0C4223B20A47D16DDC642F328CA5991C140C  5B679B8119BB5D53107C40C63DF667BAEF62DE75418C3E6B540FDBAFCCEDDCA6                              <NA>


    """
    extensions = ["." + str(x).lstrip(".").lower() for x in extensions]
    if isinstance(path, str):
        path = [path]
    allfiles = []
    for f in path:
        f = os.path.normpath(f)
        if os.path.exists(f):
            if os.path.isdir(f):
                allf = get_folder_file_complete_path(f)
                for ff in allf:
                    fff = ff.path
                    if extensions:
                        if ff.ext.lower() in extensions:
                            allfiles.append(fff)
                    else:
                        allfiles.append(fff)

            else:
                allfiles.append(f)

    allqueries = [
        [sigcheck, "-a", "-h", "-ct", "-accepteula", "-nobanner", f] for f in allfiles
    ]
    res = []
    for su in allqueries:
        try:
            res.append(
                io.StringIO(
                    subprocess.run(
                        su, capture_output=True, **invisibledict
                    ).stdout.decode("utf-8", "ignore")
                )
            )
        except Exception as fe:
            print(fe)
            continue
    allfi = [pd.read_csv(x, sep="\t", on_bad_lines="skip") for x in res]
    df = pd.concat(allfi, ignore_index=True)
    df = df.ds_reduce_memory_size_carefully(verbose=False)
    df.Date = df.Date.ds_apply_ignore(pd.NA, lambda x: pd.to_datetime(x))
    return df
