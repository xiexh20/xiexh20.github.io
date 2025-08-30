from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Xianghui", "Xie"]
    email = "xxie@mpi-inf.mpg.de"
    twitter = "Mi_Niemeyer"
    github = "m-niemeyer"
    linkedin = "michael-niemeyer"
    bio_text = f"""
                <p>
                    I am a PhD student at the <a href="https://virtualhumans.mpi-inf.mpg.de/" target="_blank">Real Virtual Humans</a> group at <a href="https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning" target="_blank">Max Planck Institute for Informatics</a> and
					<a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/fachbereich/" target="_blank">University of Tuebingen</a> under supervision of <a href="https://virtualhumans.mpi-inf.mpg.de/people/pons-moll.html" target="_blank">Prof. Dr. Gerard Pons-Moll</a>.
					I also work closely with <a href="https://janericlenssen.github.io/">Jan Eric Lessen</a>. I am interested in 3D computer vision, generative models, especially in accurate reconstruction/tracking and realistic synthesis of humans and objects.
                    
                </p>
                <p>For any inquiries or collaborations, feel free to reach out to me via mail!</p>
                <p>
                    <a href="mailto:xxie@mpi-inf.mpg.de" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://x.com/XianghuiXie" target="_blank" style="margin-right: 5px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=J3TVNXEAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/xiexh20" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://de.linkedin.com/in/xianghui-xie-3a8817198" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </div>
                </div>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This website is based on the template from <a href="https://github.com/m-niemeyer/m-niemeyer.github.io">Michael Miemeyer</a>. <br>
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kait0.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        "Gerard Pons-Moll": "https://virtualhumans.mpi-inf.mpg.de/people/pons-moll.html",
        "Jan Eric Lenssen": "https://virtualhumans.mpi-inf.mpg.de/people/Lenssen.html",
        "Yuxuan Xue": "https://yuxuan-xue.com/",
        "Ilya A. Petrov": "https://virtualhumans.mpi-inf.mpg.de/people/Petrov.html",
        "Bharat Lal Bhatnagar": "https://virtualhumans.mpi-inf.mpg.de/people/Bhatnagar.html",
        "Cristian Sminchisescu": "https://scholar.google.com/citations?user=LHTI1W8AAAAJ&hl=en",
        "Christian Theobalt": "https://www.mpi-inf.mpg.de/departments/visual-computing-and-artificial-intelligence",
        "Riccardo Marin": "riccardomarin.github.io",
        "Xianghui Xie": "https://xianghui-xie.github.io/",
        "Xianghui Xie*": "https://xianghui-xie.github.io/",
        "Bharat Lal Bhatnagar*": "https://virtualhumans.mpi-inf.mpg.de/people/Bhatnagar.html",
        "Chuhang Zou": "https://zouchuhang.github.io/"
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Xianghui Xie', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('middle') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        # if "Jan" in string_part_i:
        #     breakpoint()
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        else:
            print(f'[{string_part_i}] Warning: Author not found in author dictionary!')
        print('string_part_i', string_part_i)
        if make_bold and make_bold_name in string_part_i:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
            print('making bold for ', string_part_i)
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['image']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['website']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['website']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'website': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=True, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                        <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                        </div>
                    <br>
                    <div class="row">
                    <div class="col-md-9">
                        <p style="text-align: justify;">
                            I am a PhD student at the <a href="https://virtualhumans.mpi-inf.mpg.de/" target="_blank">Real Virtual Humans</a> group at <a href="https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning" target="_blank">Max Planck Institute for Informatics</a> and
                            <a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/fachbereich/" target="_blank">University of Tuebingen</a> under supervision of <a href="https://virtualhumans.mpi-inf.mpg.de/people/pons-moll.html" target="_blank">Prof. Dr. Gerard Pons-Moll</a>.
                            I also work closely with <a href="https://janericlenssen.github.io/">Jan Eric Lessen</a>. I am interested in 3D computer vision, generative models, especially in accurate reconstruction/tracking and realistic synthesis of humans and objects. 
                            My research goal is to create digital humans that behave like real humans and empower them with intelligence to finish daily tasks as humans do.
                        </p>
                        <p>For any inquiries or collaborations, feel free to reach out to me via mail!</p>
                        <p>
                            <a href="mailto:xxie@mpi-inf.mpg.de" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                            <a href="https://x.com/XianghuiXie" target="_blank" style="margin-right: 5px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                            <a href="https://scholar.google.com/citations?user=J3TVNXEAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                            <a href="https://github.com/xiexh20" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                            <a href="https://de.linkedin.com/in/xianghui-xie-3a8817198" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                        </p>
                    </div>
                    <div class="col-md-3">
                        <img src="assets/img/profile.jpg" class="img-thumbnail" width="320px" alt="Profile picture">
                    </div>
                    </div>

                    <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>News</h4>
                        <div style="margin-bottom: 2em;">
                            <ul style="list-style: none; padding-left: 0;">
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Aug 2025</span>
                                    <span>Two papers accepted to SIGGRAPH Asia!</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Jun 2025</span>
                                    <span>MVGBench accepted to ICCV'25, check out at <a href="https://virtualhumans.mpi-inf.mpg.de/MVGBench/" target="_blank">project page</a>.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Jun 2025</span>
                                    <span>Started research intern at NVIDIA@Santa Clara, in the learning and perception research team.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Jun 2025</span>
                                    <span>One paper accepted to TPAMI, check out <a href="https://yuxuan-xue.com/gen-3diffusion/" target="_blank">Gen-3Diffusion</a>.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Nov 2024</span>
                                    <span>One paper accepted to 3DV. See <a href="https://virtualhumans.mpi-inf.mpg.de/InterTrack/" target="_blank">InterTrack</a>.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Sep 2024</span>
                                    <span>One paper accepted to NeurIPS, checkout <a href="https://yuxuan-xue.com/human-3diffusion/" target="_blank">Human3Diffusion</a>.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Aug 2024</span>
                                    <span>Started research internship at Amazon.</span>
                                </li>
                                <li style="margin-bottom: 0.5em;">
                                    <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Feb 2024</span>
                                    <span>One paper accepted to CVPR as <span style="color: red; font-weight: bold;">highlight</span>, checkout <a href="https://virtualhumans.mpi-inf.mpg.de/procigen-hdm/" target="_blank">ProciGen</a>.</span>
                                </li>
                            </ul>
                            
                            <!-- Collapsible additional news -->
                            <div class="collapse" id="collapseMoreNews">
                                <ul style="list-style: none; padding-left: 0;">
                                    <li style="margin-bottom: 0.5em;">
                                        <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Feb 2023</span>
                                        <span>One paper accepted to CVPR'23, checkout <a href="/VisTracker/" target="_blank">VisTracker</a>.</span>
                                    </li>
                                    <li style="margin-bottom: 0.5em;">
                                        <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Jul 2022</span>
                                        <span>CHORE paper accepted to ECCV'22, checkout <a href="/chore/" target="_blank">CHORE</a>.</span>
                                    </li>
                                    <li style="margin-bottom: 0.5em;">
                                        <span style="color: #6c757d; font-weight: bold; display: inline-block; width: 80px;">Feb 2022</span>
                                        <span>BEHAVE accepted to CVPR'22, see <a href="/behave/" target="_blank">BEHAVE</a>.</span>
                                    </li>
                                </ul>
                            </div>
                            
                            <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapseMoreNews" aria-expanded="false" aria-controls="collapseMoreNews" style="color: #007bff; font-size: 0.9em; padding: 0; margin-left: -6px;">
                                <span class="show-more-text">Show more</span>
                                <span class="show-less-text" style="display: none;">Show less</span>
                            </button>
                        </div>
                    </div>


                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Talks</h4>
                        {talks}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
