using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.IO;
using System.Text;
using WebApp.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net.Http;
using System.Configuration;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;
using WebApp.Client;

namespace WebApp.Controllers
{
    public class HomeController : Controller
    {
        static string baseFileName = "outFile4";
        string uploadFilePath = @"C:\Users\M1039179\Desktop\";
        string pythonExePath = @"C:\Windows\py.exe";
        string cmdFile = @"cmd.exe";
        string imageSegmentation = @"D:\Osmosis-2020\Main\models-1.13.0\research\object_detection\object_detection_tutorial.py";
        string testImagesBasePath = @"D:\Osmosis-2020\Main\models-1.13.0\research\object_detection\test_images\";
        string pythonCallingScript = @"D:\Osmosis-2020\Main\models-1.13.0\research\object_detection\execPyScript.py";
        string temp = @"D:\Osmosis-2020\Main\Application\WebApp\WebApp\models-1.13.0\research\object_detection\object_detection_tutorial.py";
        string pythonExeFile2 = @"C:\Users\M1039179\AppData\Local\Programs\Python\Python35\python.exe";
        // GET: Home
        public ActionResult Index()
        {
            //WSDDisplay();
            return View();
        }

        [HttpPost]
        public async Task<ActionResult> Index(HttpPostedFileBase file)
        {
            try
            {
                if (file.ContentLength > 0)
                {
                    string _FileName = Path.GetFileName(file.FileName);
                    string _path = Path.Combine(testImagesBasePath, "image0.jpg");
                    file.SaveAs(_path);
                }
                //ProcessUpload();
                //run_cmd();
                //var value = await ProcessImageSegmentation();

                HttpClientHelper.SegmentImages();
                List<string> productsList = System.IO.File.ReadLines(Server.MapPath("~") + "/ProcessedFiles/products.txt").ToList();
                List<MatchedProduct> MatchedProducts = new List<MatchedProduct>();
                foreach (var product in productsList)
                {
                    var mp = HttpClientHelper.ProductMatcher(product);
                    if (mp != null)
                    {
                        MatchedProducts.Add(mp);
                    }

                }
                string companyInfo = String.Join("", System.IO.File.ReadLines(Server.MapPath("~") + "/ProcessedFiles/companyName.txt").ToList());
                var companyName = HttpClientHelper.CompanyMatcher(companyInfo);
                ViewBag.CompanyName = companyName;
                //System.Threading.Thread.Sleep(10000);
                //using (StreamReader r = new StreamReader(Server.MapPath("~") + "\\Data\\masterDB.json"))
                //{
                //    string json = r.ReadToEnd();
                //    var items = JsonConvert.DeserializeObject<List<MasterDB>>(json);
                //    var i = 0;
                //}

                return View("WSDDisplay", MatchedProducts);
            }
            catch (Exception ex)
            {
                //ViewBag.Message = "File upload failed!!";
                return View("WSDDisplay");
            }
        }

        [HttpGet]
        public ActionResult WSDDisplay(InputTxt inputTxt)
        {
            //string mainInputText = "", mainInputLinkText = "";
            //var filePath = "";
            //if(inputTxt.InputUploadValue != null && inputTxt.InputUploadValue != string.Empty){
            //    mainInputText = ReadFromFile(uploadFilePath + inputTxt.InputUploadValue);
            //}
            //else if(inputTxt.InputTextValue != null && inputTxt.InputTextValue != string.Empty)
            //{
            //    mainInputText = inputTxt.InputTextValue;
            //}
            //else if(inputTxt.InputLinkValue != null && inputTxt.InputLinkValue != string.Empty)
            //{
            //    mainInputLinkText = inputTxt.InputLinkValue;
            //}

            //var obj = JSON.parse(Server.MapPath("~") + "\\Data\\masterDB.json");
            //using (StreamReader r = new StreamReader(Server.MapPath("~") + "\\Data\\masterDB.json"))
            //{
            //    string json = r.ReadToEnd();
            //    var items = JsonConvert.DeserializeObject<List<MasterDB>>(json);
            //    var i = 0;
            //}
            return View();
        }

        private string ReadFromFile(string filePath)
        {
            string text = "";
            var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);

            using (var streamReader = new StreamReader(fileStream, Encoding.UTF8))
            {
                text = streamReader.ReadToEnd();
            }

            return text;
        }
        private async Task<int> ProcessImageSegmentation()
        {
            System.Diagnostics.Process.Start(Server.MapPath("~") + "models-1.13.0\\research\\object_detection\\object_detection_tutorial.py");

            var p = System.Diagnostics.Process.Start(temp);
            p.WaitForExit();

            ScriptEngine engine = Python.CreateEngine();
            engine.ExecuteFile(imageSegmentation);
            
            return 1;
        }

        private void run_cmd()
        {
            string fileName = imageSegmentation;
            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(pythonExePath, fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();
        }

        private void ProcessUpload()
        {
            
        }
    }
}