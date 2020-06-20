uses graphabc;
uses System.IO, System.Net;

var fr,en:integer;
var gbuff := new queue <integer>;

function stdreq(path:string):string;
var 
  html : string;
  url : string := 'http://127.0.0.1:2938/';
begin
  url+=path;
  var myRequest : HttpWebRequest := HttpWebRequest(WebRequest.Create(url));
  myRequest.Method := 'GET';
  var myResponse : WebResponse := myRequest.GetResponse();
  var sr : StreamReader := new StreamReader(myResponse.GetResponseStream(), System.Text.Encoding.UTF8);
  html := sr.ReadToEnd();
  sr.Close();
  myResponse.Close();
  stdreq:=html;
end;

function req(path:string):string;
begin
 var s:string;
 try
  s:=stdreq(fr.tostring()+'z'+en.tostring()+'z'+path);
 except
  halt;
 end;
 foreach w:string in s.split('a') do
 begin
  var d:=0;
  if integer.tryparse(w,d) then
  gbuff.enqueue(d);
 end;
end;

procedure post(q:int64);
begin
 req(q.tostring()+'a');
end;

procedure post(q:color);
begin
 post(getred(q));
 post(getgreen(q));
 post(getblue(q)); 
end;

procedure post();
begin
 req('');
end;

function get():integer;
begin
 while gbuff.count=0 do begin
   req('');
   sleep(100);
 end;
 var g:=gbuff.dequeue();
 get:=g;
end;

function get_integet():integer;
begin
 get_integer:=get();
end;

function get_color():color;
begin
 get_color:=rgb(get(),get(),get());
end;

procedure putpixel_h();
begin
putpixel(get(),get(),rgb(get(),get(),get()));
end;

procedure getpixel_h();
begin
post(getpixel(get(),get()));
end;

begin
var s:=stdreq('');
integer.tryparse(s,fr);
fr-=1;
en:=fr-1;
var com:=0;
///////////////////////
while true do
begin
 com:=get();
 if com=0 then
  putpixel_h();
 if com=1 then
  getpixel_h();
end;
///////////////////////
end.
