import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re
import os


class VKConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("VK虚拟键值转换器")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        
        self.vk_data = {}
        self.reverse_data = {}
        self.alias_map = {}
        self.load_vk_data()
        self.init_alias_map()
        
        self.create_widgets()
    
    def load_vk_data(self):
        md_path = os.path.join(os.path.dirname(__file__), "VK虚拟键值表.md")
        if not os.path.exists(md_path):
            messagebox.showerror("错误", "找不到 VK虚拟键值表.md 文件")
            return
        
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines[2:]:
            line = line.strip()
            if not line or line.startswith('| ---'):
                continue
            
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 2:
                name = parts[0].strip('`')
                hex_val = parts[1].strip()
                desc = parts[2] if len(parts) > 2 else ""
                
                if name and hex_val and not hex_val.startswith('0x'):
                    continue
                
                if name and re.match(r'^0x[0-9A-Fa-f]{2}(-[0-9A-Fa-f]{2})?$', hex_val):
                    self.vk_data[name] = {'hex': hex_val, 'desc': desc}
                    
                    main_hex = hex_val.split('-')[0]
                    self.reverse_data[main_hex.upper()] = {'name': name, 'desc': desc}
                    self.reverse_data[main_hex.lower()] = {'name': name, 'desc': desc}
                    
                    if name.startswith('VK_'):
                        self.reverse_data[name] = {'hex': hex_val, 'desc': desc}
    
    def init_alias_map(self):
        self.alias_map = {
            'ENTER': 'VK_RETURN',
            'RETURN': 'VK_RETURN',
            'TAB': 'VK_TAB',
            'ESC': 'VK_ESCAPE',
            'ESCAPE': 'VK_ESCAPE',
            'SPACE': 'VK_SPACE',
            'BACKSPACE': 'VK_BACK',
            'BKSP': 'VK_BACK',
            'DELETE': 'VK_DELETE',
            'DEL': 'VK_DELETE',
            'INSERT': 'VK_INSERT',
            'INS': 'VK_INSERT',
            'HOME': 'VK_HOME',
            'END': 'VK_END',
            'PAGEUP': 'VK_PRIOR',
            'PGUP': 'VK_PRIOR',
            'PAGEDOWN': 'VK_NEXT',
            'PGDN': 'VK_NEXT',
            'UP': 'VK_UP',
            'DOWN': 'VK_DOWN',
            'LEFT': 'VK_LEFT',
            'RIGHT': 'VK_RIGHT',
            '↑': 'VK_UP',
            '↓': 'VK_DOWN',
            '←': 'VK_LEFT',
            '→': 'VK_RIGHT',
            'CTRL': 'VK_CONTROL',
            'CTRL_L': 'VK_LCONTROL',
            'CTRL_R': 'VK_RCONTROL',
            'LCTRL': 'VK_LCONTROL',
            'RCTRL': 'VK_RCONTROL',
            'SHIFT': 'VK_SHIFT',
            'SHIFT_L': 'VK_LSHIFT',
            'SHIFT_R': 'VK_RSHIFT',
            'LSHIFT': 'VK_LSHIFT',
            'RSHIFT': 'VK_RSHIFT',
            'ALT': 'VK_MENU',
            'ALT_L': 'VK_LMENU',
            'ALT_R': 'VK_RMENU',
            'LALT': 'VK_LMENU',
            'RALT': 'VK_RMENU',
            'MENU': 'VK_MENU',
            'WIN': 'VK_LWIN',
            'WIN_L': 'VK_LWIN',
            'WIN_R': 'VK_RWIN',
            'LWIN': 'VK_LWIN',
            'RWIN': 'VK_RWIN',
            'CAPSLOCK': 'VK_CAPITAL',
            'CAPS': 'VK_CAPITAL',
            'NUMLOCK': 'VK_NUMLOCK',
            'SCROLLLOCK': 'VK_SCROLL',
            'PRINTSCREEN': 'VK_SNAPSHOT',
            'PRTSC': 'VK_SNAPSHOT',
            'PAUSE': 'VK_PAUSE',
            'BREAK': 'VK_PAUSE',
            'F1': 'VK_F1',
            'F2': 'VK_F2',
            'F3': 'VK_F3',
            'F4': 'VK_F4',
            'F5': 'VK_F5',
            'F6': 'VK_F6',
            'F7': 'VK_F7',
            'F8': 'VK_F8',
            'F9': 'VK_F9',
            'F10': 'VK_F10',
            'F11': 'VK_F11',
            'F12': 'VK_F12',
            'NUMPAD0': 'VK_NUMPAD0',
            'NUMPAD1': 'VK_NUMPAD1',
            'NUMPAD2': 'VK_NUMPAD2',
            'NUMPAD3': 'VK_NUMPAD3',
            'NUMPAD4': 'VK_NUMPAD4',
            'NUMPAD5': 'VK_NUMPAD5',
            'NUMPAD6': 'VK_NUMPAD6',
            'NUMPAD7': 'VK_NUMPAD7',
            'NUMPAD8': 'VK_NUMPAD8',
            'NUMPAD9': 'VK_NUMPAD9',
            'NP0': 'VK_NUMPAD0',
            'NP1': 'VK_NUMPAD1',
            'NP2': 'VK_NUMPAD2',
            'NP3': 'VK_NUMPAD3',
            'NP4': 'VK_NUMPAD4',
            'NP5': 'VK_NUMPAD5',
            'NP6': 'VK_NUMPAD6',
            'NP7': 'VK_NUMPAD7',
            'NP8': 'VK_NUMPAD8',
            'NP9': 'VK_NUMPAD9',
            'NPMUL': 'VK_MULTIPLY',
            'NPADD': 'VK_ADD',
            'NPSUB': 'VK_SUBTRACT',
            'NPDEC': 'VK_DECIMAL',
            'NPDIV': 'VK_DIVIDE',
            'MULTIPLY': 'VK_MULTIPLY',
            'ADD': 'VK_ADD',
            'SUBTRACT': 'VK_SUBTRACT',
            'DECIMAL': 'VK_DECIMAL',
            'DIVIDE': 'VK_DIVIDE',
            'APPS': 'VK_APPS',
            'SLEEP': 'VK_SLEEP',
            'BROWSER_BACK': 'VK_BROWSER_BACK',
            'BROWSER_FORWARD': 'VK_BROWSER_FORWARD',
            'BROWSER_REFRESH': 'VK_BROWSER_REFRESH',
            'BROWSER_STOP': 'VK_BROWSER_STOP',
            'BROWSER_SEARCH': 'VK_BROWSER_SEARCH',
            'BROWSER_FAVORITES': 'VK_BROWSER_FAVORITES',
            'BROWSER_HOME': 'VK_BROWSER_HOME',
            'VOLUME_MUTE': 'VK_VOLUME_MUTE',
            'VOLUME_DOWN': 'VK_VOLUME_DOWN',
            'VOLUME_UP': 'VK_VOLUME_UP',
            'MEDIA_NEXT': 'VK_MEDIA_NEXT_TRACK',
            'MEDIA_PREV': 'VK_MEDIA_PREV_TRACK',
            'MEDIA_STOP': 'VK_MEDIA_STOP',
            'MEDIA_PLAY_PAUSE': 'VK_MEDIA_PLAY_PAUSE',
            'LAUNCH_MAIL': 'VK_LAUNCH_MAIL',
            'LAUNCH_MEDIA': 'VK_LAUNCH_MEDIA_SELECT',
            'LAUNCH_APP1': 'VK_LAUNCH_APP1',
            'LAUNCH_APP2': 'VK_LAUNCH_APP2',
        }
    
    def parse_key_sequence(self, text):
        results = []
        pattern = r'\[([^\]]+)\]'
        last_end = 0
        
        for match in re.finditer(pattern, text):
            if match.start() > last_end:
                plain = text[last_end:match.start()].strip()
                if plain:
                    results.append({'type': 'text', 'content': plain})
            
            key_name = match.group(1).strip()
            
            paste_match = re.match(r'Pasted\s+~(\d+)\s+line', key_name, re.IGNORECASE)
            if paste_match:
                line_count = paste_match.group(1)
                results.append({'type': 'paste', 'content': f'粘贴 {line_count} 行'})
                last_end = match.end()
                continue
            
            key_upper = key_name.upper().replace('-', '_').replace(' ', '_')
            vk_name = self.alias_map.get(key_upper)
            
            if not vk_name:
                for alias, vk in self.alias_map.items():
                    if alias in key_upper or key_upper in alias:
                        vk_name = vk
                        break
            
            if vk_name and vk_name in self.vk_data:
                hex_val = self.vk_data[vk_name]['hex']
                desc = self.vk_data[vk_name]['desc']
                results.append({
                    'type': 'key',
                    'alias': key_name,
                    'vk_name': vk_name,
                    'hex': hex_val,
                    'desc': desc
                })
            else:
                results.append({'type': 'unknown', 'content': key_name})
            
            last_end = match.end()
        
        if last_end < len(text):
            plain = text[last_end:].strip()
            if plain:
                results.append({'type': 'text', 'content': plain})
        
        return results
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        self.create_single_tab()
        self.create_sequence_tab()
    
    def create_single_tab(self):
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="单键转换")
        
        tab.columnconfigure(1, weight=1)
        
        title_label = ttk.Label(tab, text="VK虚拟键值转换器", font=("微软雅黑", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))
        
        ttk.Label(tab, text="输入VK名称或十六进制值:", font=("微软雅黑", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(tab, textvariable=self.input_var, font=("Consolas", 12))
        self.input_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        self.input_entry.bind('<Return>', lambda e: self.convert())
        
        self.convert_btn = ttk.Button(tab, text="转换", command=self.convert)
        self.convert_btn.grid(row=1, column=2, pady=5)
        
        result_frame = ttk.LabelFrame(tab, text="转换结果", padding="10")
        result_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=15)
        result_frame.columnconfigure(1, weight=1)
        
        ttk.Label(result_frame, text="VK名称:", font=("微软雅黑", 10)).grid(row=0, column=0, sticky=tk.W, pady=3)
        self.result_name = ttk.Label(result_frame, text="", font=("Consolas", 12), foreground="blue")
        self.result_name.grid(row=0, column=1, sticky=tk.W, pady=3)
        
        ttk.Label(result_frame, text="十六进制值:", font=("微软雅黑", 10)).grid(row=1, column=0, sticky=tk.W, pady=3)
        self.result_hex = ttk.Label(result_frame, text="", font=("Consolas", 12), foreground="green")
        self.result_hex.grid(row=1, column=1, sticky=tk.W, pady=3)
        
        ttk.Label(result_frame, text="十进制值:", font=("微软雅黑", 10)).grid(row=2, column=0, sticky=tk.W, pady=3)
        self.result_dec = ttk.Label(result_frame, text="", font=("Consolas", 12), foreground="purple")
        self.result_dec.grid(row=2, column=1, sticky=tk.W, pady=3)
        
        ttk.Label(result_frame, text="描述:", font=("微软雅黑", 10)).grid(row=3, column=0, sticky=tk.W, pady=3)
        self.result_desc = ttk.Label(result_frame, text="", font=("微软雅黑", 10), wraplength=500)
        self.result_desc.grid(row=3, column=1, sticky=tk.W, pady=3)
        
        ttk.Label(tab, text="搜索/浏览:", font=("微软雅黑", 10)).grid(row=3, column=0, sticky=tk.W, pady=5)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(tab, textvariable=self.search_var, font=("微软雅黑", 10))
        self.search_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.on_search)
        
        list_frame = ttk.Frame(tab)
        list_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        columns = ('name', 'hex', 'dec', 'desc')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=12)
        
        self.tree.heading('name', text='VK名称')
        self.tree.heading('hex', text='十六进制')
        self.tree.heading('dec', text='十进制')
        self.tree.heading('desc', text='描述')
        
        self.tree.column('name', width=150)
        self.tree.column('hex', width=80)
        self.tree.column('dec', width=80)
        self.tree.column('desc', width=400)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
        
        self.populate_tree()
        
        tab.rowconfigure(4, weight=1)
    
    def create_sequence_tab(self):
        tab = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(tab, text="按键序列解析")
        
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(1, weight=1)
        tab.rowconfigure(3, weight=1)
        
        ttk.Label(tab, text="粘贴按键序列数据:", font=("微软雅黑", 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.seq_input = scrolledtext.ScrolledText(tab, font=("Consolas", 11), height=6, wrap=tk.WORD)
        self.seq_input.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.seq_input.insert('1.0', '[Pasted ~4 linecmd[ENTER]\n[CTRL_L]pyinstaller [ENTER]\n[↑]-h[ENTER]')
        
        btn_frame = ttk.Frame(tab)
        btn_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(btn_frame, text="解析序列", command=self.parse_sequence).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="清空", command=self.clear_sequence).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(tab, text="解析结果:", font=("微软雅黑", 10)).grid(row=2, column=0, sticky=tk.W, pady=(60, 5))
        
        result_frame = ttk.Frame(tab)
        result_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        result_frame.columnconfigure(0, weight=1)
        result_frame.rowconfigure(0, weight=1)
        
        columns = ('pos', 'type', 'alias', 'vk_name', 'hex', 'dec', 'desc')
        self.seq_tree = ttk.Treeview(result_frame, columns=columns, show='headings', height=12)
        
        self.seq_tree.heading('pos', text='#')
        self.seq_tree.heading('type', text='类型')
        self.seq_tree.heading('alias', text='输入')
        self.seq_tree.heading('vk_name', text='VK名称')
        self.seq_tree.heading('hex', text='十六进制')
        self.seq_tree.heading('dec', text='十进制')
        self.seq_tree.heading('desc', text='描述')
        
        self.seq_tree.column('pos', width=40)
        self.seq_tree.column('type', width=60)
        self.seq_tree.column('alias', width=120)
        self.seq_tree.column('vk_name', width=140)
        self.seq_tree.column('hex', width=70)
        self.seq_tree.column('dec', width=60)
        self.seq_tree.column('desc', width=300)
        
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.seq_tree.yview)
        self.seq_tree.configure(yscrollcommand=scrollbar.set)
        
        self.seq_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    def populate_tree(self, filter_text=""):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for name, data in sorted(self.vk_data.items()):
            hex_val = data['hex']
            desc = data['desc']
            
            main_hex = hex_val.split('-')[0]
            try:
                dec_val = str(int(main_hex, 16))
            except ValueError:
                dec_val = ""
            
            if filter_text:
                filter_lower = filter_text.lower()
                if (filter_lower not in name.lower() and 
                    filter_lower not in hex_val.lower() and 
                    filter_lower not in desc.lower()):
                    continue
            
            self.tree.insert('', tk.END, values=(name, hex_val, dec_val, desc))
    
    def convert(self):
        input_text = self.input_var.get().strip()
        if not input_text:
            messagebox.showwarning("警告", "请输入VK名称或十六进制值")
            return
        
        if input_text.upper().startswith('VK_') or input_text.upper().startswith('VK'):
            if not input_text.upper().startswith('VK_'):
                input_text = 'VK_' + input_text[2:]
            
            if input_text in self.vk_data:
                data = self.vk_data[input_text]
                hex_val = data['hex']
                main_hex = hex_val.split('-')[0]
                try:
                    dec_val = str(int(main_hex, 16))
                except ValueError:
                    dec_val = ""
                
                self.result_name.config(text=input_text)
                self.result_hex.config(text=hex_val)
                self.result_dec.config(text=dec_val)
                self.result_desc.config(text=data['desc'])
            else:
                messagebox.showinfo("结果", f"未找到VK名称: {input_text}")
        
        elif input_text.startswith('0x') or input_text.startswith('0X'):
            hex_val = input_text.upper()
            if hex_val in self.reverse_data:
                data = self.reverse_data[hex_val]
                main_hex = hex_val.replace('0X', '0x')
                try:
                    dec_val = str(int(main_hex, 16))
                except ValueError:
                    dec_val = ""
                
                self.result_name.config(text=data['name'])
                self.result_hex.config(text=main_hex)
                self.result_dec.config(text=dec_val)
                self.result_desc.config(text=data['desc'])
            else:
                try:
                    dec_val = str(int(input_text, 16))
                    self.result_name.config(text="未知")
                    self.result_hex.config(text=input_text)
                    self.result_dec.config(text=dec_val)
                    self.result_desc.config(text="未找到对应的VK名称")
                except ValueError:
                    messagebox.showerror("错误", "无效的十六进制值")
        
        else:
            try:
                if input_text.isdigit():
                    dec_val = int(input_text)
                    hex_val = f"0x{dec_val:02X}"
                    
                    if hex_val in self.reverse_data:
                        data = self.reverse_data[hex_val]
                        self.result_name.config(text=data['name'])
                        self.result_hex.config(text=hex_val)
                        self.result_dec.config(text=str(dec_val))
                        self.result_desc.config(text=data['desc'])
                    else:
                        self.result_name.config(text="未知")
                        self.result_hex.config(text=hex_val)
                        self.result_dec.config(text=str(dec_val))
                        self.result_desc.config(text="未找到对应的VK名称")
                else:
                    found = False
                    for name, data in self.vk_data.items():
                        if input_text.upper() in name.upper() or input_text in data['desc']:
                            hex_val = data['hex']
                            main_hex = hex_val.split('-')[0]
                            try:
                                dec_val = str(int(main_hex, 16))
                            except ValueError:
                                dec_val = ""
                            
                            self.result_name.config(text=name)
                            self.result_hex.config(text=hex_val)
                            self.result_dec.config(text=dec_val)
                            self.result_desc.config(text=data['desc'])
                            found = True
                            break
                    
                    if not found:
                        messagebox.showinfo("结果", f"未找到匹配: {input_text}")
            except Exception as e:
                messagebox.showerror("错误", f"转换失败: {str(e)}")
    
    def on_search(self, event=None):
        filter_text = self.search_var.get().strip()
        self.populate_tree(filter_text)
    
    def on_tree_select(self, event=None):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            if values:
                self.result_name.config(text=values[0])
                self.result_hex.config(text=values[1])
                self.result_dec.config(text=values[2])
                self.result_desc.config(text=values[3])
                self.input_var.set(values[0])
    
    def parse_sequence(self):
        for item in self.seq_tree.get_children():
            self.seq_tree.delete(item)
        
        input_text = self.seq_input.get('1.0', tk.END).strip()
        if not input_text:
            messagebox.showwarning("警告", "请输入按键序列")
            return
        
        lines = input_text.split('\n')
        pos = 1
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            results = self.parse_key_sequence(line)
            
            for r in results:
                if r['type'] == 'key':
                    main_hex = r['hex'].split('-')[0]
                    try:
                        dec_val = str(int(main_hex, 16))
                    except ValueError:
                        dec_val = ""
                    
                    self.seq_tree.insert('', tk.END, values=(
                        pos, '按键', r['alias'], r['vk_name'], r['hex'], dec_val, r['desc']
                    ))
                elif r['type'] == 'paste':
                    self.seq_tree.insert('', tk.END, values=(
                        pos, '粘贴', r['content'], '-', '-', '-', '-'
                    ))
                elif r['type'] == 'text':
                    self.seq_tree.insert('', tk.END, values=(
                        pos, '文本', r['content'], '-', '-', '-', '-'
                    ))
                elif r['type'] == 'unknown':
                    self.seq_tree.insert('', tk.END, values=(
                        pos, '未知', r['content'], '-', '-', '-', '无法识别的按键'
                    ))
                
                pos += 1
    
    def clear_sequence(self):
        self.seq_input.delete('1.0', tk.END)
        for item in self.seq_tree.get_children():
            self.seq_tree.delete(item)


def main():
    root = tk.Tk()
    app = VKConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()