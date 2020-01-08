from django import forms
from django.forms import formset_factory
from django.forms import BaseFormSet

class tclInput(forms.Form):
    meshFile = forms.FileField(label='Mesh File')
    kernelType = forms.ChoiceField(label='Kernel Type', choices=(('TetraSVKernal','TetraSVKernel'),
                                                           ('TetraSurfaceKernal','TetraSurfaceKernel'),
                                                           ('TetraVolumeKernal','TetraVolumeKernel'),
                                                           ('TetraInternalKernal','TetraInternalKernel')))

class materialSet(forms.Form):
    material = forms.CharField(label='Material',
                               widget=forms.TextInput(attrs={
                                                      'class': 'form-control',
                                                      'placeholder': 'Enter Material Name here'
                                                      }),
                               max_length=255)
    scatteringCoeff = forms.FloatField(label='Scattering Coefficient', min_value=0)
    absorptionCoeff = forms.FloatField(label='Absorption Coefficient', min_value=0)
    refractiveIndex = forms.FloatField(label='Refractive Index', min_value=0)
    anisotropy = forms.FloatField(label='Anisotropy', min_value=0)

class lightSource(forms.Form):
    sourceType = forms.ChoiceField(label='Type', choices=(('point','Point'),
                                                            ('pencilbeam','PencilBeam'),
                                                            ('volume','Volume'),
                                                            ('ball','Ball'),
                                                            ('line','Line'),
                                                            ('fiber','Fiber'),
                                                            ('tetraface','Tetraface'),
                                                            ('cylinder','Cylinder'),
                                                            ('composite','Composite')))
    xPos = forms.FloatField(label='X Position')
    yPos = forms.FloatField(label='Y Position')
    zPos = forms.FloatField(label='Z Position')
    power = forms.IntegerField(label='Power')

class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

materialSetSet = formset_factory(materialSet, formset=RequiredFormSet)
lightSourceSet = formset_factory(lightSource, formset=RequiredFormSet)
