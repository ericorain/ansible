''' Well just an import '''
unsAnsible = '''
01. The first lie of Ansible is to make people believe that they are not doing programing; yaml language is declarative programing and the Ansible yang version has a bit of imperative programing

02. With Ansible we do not focus on how to achieve our goal but on how to do it with Ansible

03. People believe it is fast to write Ansible "programs" just because they forgot to look at their clock

04. Ansible playbooks are not easy to write since they use DSL, something additional to learn

05. Ansible is more complex to understand than many other frameworks since it uses at least 2 languages

06. Debugging with Ansible is a nightmare

07. Ansible is not the only solution for network engineer as a framework

08. Ansible does not have the flexibility python has

09. Ansible is not fast when it is about a lot of network devices

10. When something is easy to do then we can do it without Ansible with less effort

11. And when something is hard to do we can also skip Ansible since it will be even harder than with other frameworks

12. What we learn in Ansible "language" is not knowledge we can reuse in another programing language

13. Ansible forces us to install python but python does not force us to use Ansible

14. Ansible requires more files than the python frameworks it uses to achieve the same goal (Ansible+Ansible module+python+python libraries+hosts 
file+config file+playbook = 7 vs python+python libraries+python scripts = 3)

15. "Ansible is not a programming language. But as use-cases grow more complex, playbook writers start to look for programmatic features. Stop it. 
Sometimes just bite the bullet and write some Python to extend Jinja. The Ansible abstraction has limits. That's what keeps it simple."  jag on Twitter

16. "unless you're writing modules or plugins, you don't get the full expressive power of Python, you get the weird sort-of-Python that is Jinja.", nfirvine from http://blog.nfi.io

17. The print output of the result of Ansible playbooks is difficult to modify whereas it is so easy in many programing languages

18. By default "gather_facts: True" on playbooks... to be sure to slow down speed? Just crazy logic.

19. Ansible was not designed for network engineer needs

20. Ansible ping is confusing for network engineers: it uses SSH or if it fails it uses SFTP then SCP

21. If you are neither a hipster nor a fashion victim then you do not need Ansible

22. Ansible uses Python. If Python deprecates functions all Ansible modules using that function need to be rewritten; all of those modules!

23. Many people believe network automation is just and only Ansible because worldwide training centers just propose that option for network automation and also because google searches bring them to Red Hat Web site. People should not believe marketing attracting advertisement...

24. Many people believe Ansible is a magic box. Magic does not exist in networking.

25. Ansible is a way to make Dmitry talking for 30 minutes; so... really... just for him do not spread the word about Ansible ;)

'''
print(unsAnsible)

