# dejce



针对 https://github.com/Ch1ngg/JCE 的自动脱混淆脚本。

可能会在实际项目中用到，先写出来 以备后用。



usage:

```shell
python3 dejce.py -i infile.jsp -o outfile.jsp
```



假如我们在流量中 或者实际落地文件中看到jsp文件中包含有大量诸如\u00xx,<![CDATA[x]]>,&#xx 此类字符。可以通过此脚本一键脱混淆。方便查看真实逻辑。