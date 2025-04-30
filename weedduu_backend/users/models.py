from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from os import path
from django.conf import settings
from .manager import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import  PermissionsMixin






def get_profile_picture_filepath(instance, filename):
    filename = filename.split('.')[-1]
    return path.join('profile_images/', '{}profile_image.{}'.format(instance.pk, filename))

countries_option = [
    ('AF', u'Afghanistan'),
    ('AX', u'\xc5land Islands'),
    ('AL', u'Albania'),
    ('DZ', u'Algeria'),
    ('AS', u'American Samoa'),
    ('AD', u'Andorra'),
    ('AO', u'Angola'),
    ('AI', u'Anguilla'),
    ('AQ', u'Antarctica'),
    ('AG', u'Antigua and Barbuda'),
    ('AR', u'Argentina'),
    ('AM', u'Armenia'),
    ('AW', u'Aruba'),
    ('AU', u'Australia'),
    ('AT', u'Austria'),
    ('AZ', u'Azerbaijan'),
    ('BS', u'Bahamas'),
    ('BH', u'Bahrain'),
    ('BD', u'Bangladesh'),
    ('BB', u'Barbados'),
    ('BY', u'Belarus'),
    ('BE', u'Belgium'),
    ('BZ', u'Belize'),
    ('BJ', u'Benin'),
    ('BM', u'Bermuda'),
    ('BT', u'Bhutan'),
    ('BO', u'Bolivia, Plurinational State of'),
    ('BQ', u'Bonaire, Sint Eustatius and Saba'),
    ('BA', u'Bosnia and Herzegovina'),
    ('BW', u'Botswana'),
    ('BV', u'Bouvet Island'),
    ('BR', u'Brazil'),
    ('IO', u'British Indian Ocean Territory'),
    ('BN', u'Brunei Darussalam'),
    ('BG', u'Bulgaria'),
    ('BF', u'Burkina Faso'),
    ('BI', u'Burundi'),
    ('KH', u'Cambodia'),
    ('CM', u'Cameroon'),
    ('CA', u'Canada'),
    ('CV', u'Cape Verde'),
    ('KY', u'Cayman Islands'),
    ('CF', u'Central African Republic'),
    ('TD', u'Chad'),
    ('CL', u'Chile'),
    ('CN', u'China'),
    ('CX', u'Christmas Island'),
    ('CC', u'Cocos (Keeling Islands)'),
    ('CO', u'Colombia'),
    ('KM', u'Comoros'),
    ('CG', u'Congo'),
    ('CD', u'Congo, The Democratic Republic of the'),
    ('CK', u'Cook Islands'),
    ('CR', u'Costa Rica'),
    ('CI', u"C\xf4te D'ivoire"),
    ('HR', u'Croatia'),
    ('CU', u'Cuba'),
    ('CW', u'Cura\xe7ao'),
    ('CY', u'Cyprus'),
    ('CZ', u'Czech Republic'),
    ('DK', u'Denmark'),
    ('DJ', u'Djibouti'),
    ('DM', u'Dominica'),
    ('DO', u'Dominican Republic'),
    ('EC', u'Ecuador'),
    ('EG', u'Egypt'),
    ('SV', u'El Salvador'),
    ('GQ', u'Equatorial Guinea'),
    ('ER', u'Eritrea'),
    ('EE', u'Estonia'),
    ('ET', u'Ethiopia'),
    ('FK', u'Falkland Islands (Malvinas)'),
    ('FO', u'Faroe Islands'),
    ('FJ', u'Fiji'),
    ('FI', u'Finland'),
    ('FR', u'France'),
    ('GF', u'French Guiana'),
    ('PF', u'French Polynesia'),
    ('TF', u'French Southern Territories'),
    ('GA', u'Gabon'),
    ('GM', u'Gambia'),
    ('GE', u'Georgia'),
    ('DE', u'Germany'),
    ('GH', u'Ghana'),
    ('GI', u'Gibraltar'),
    ('GR', u'Greece'),
    ('GL', u'Greenland'),
    ('GD', u'Grenada'),
    ('GP', u'Guadeloupe'),
    ('GU', u'Guam'),
    ('GT', u'Guatemala'),
    ('GG', u'Guernsey'),
    ('GN', u'Guinea'),
    ('GW', u'Guinea-bissau'),
    ('GY', u'Guyana'),
    ('HT', u'Haiti'),
    ('HM', u'Heard Island and McDonald Islands'),
    ('VA', u'Holy See (Vatican City State)'),
    ('HN', u'Honduras'),
    ('HK', u'Hong Kong'),
    ('HU', u'Hungary'),
    ('IS', u'Iceland'),
    ('IN', u'India'),
    ('ID', u'Indonesia'),
    ('IR', u'Iran, Islamic Republic of'),
    ('IQ', u'Iraq'),
    ('IE', u'Ireland'),
    ('IM', u'Isle of Man'),
    ('IL', u'Israel'),
    ('IT', u'Italy'),
    ('JM', u'Jamaica'),
    ('JP', u'Japan'),
    ('JE', u'Jersey'),
    ('JO', u'Jordan'),
    ('KZ', u'Kazakhstan'),
    ('KE', u'Kenya'),
    ('KI', u'Kiribati'),
    ('KP', u"Korea, Democratic People's Republic of"),
    ('KR', u'Korea, Republic of'),
    ('KW', u'Kuwait'),
    ('KG', u'Kyrgyzstan'),
    ('LA', u"Lao People's Democratic Republic"),
    ('LV', u'Latvia'),
    ('LB', u'Lebanon'),
    ('LS', u'Lesotho'),
    ('LR', u'Liberia'),
    ('LY', u'Libya'),
    ('LI', u'Liechtenstein'),
    ('LT', u'Lithuania'),
    ('LU', u'Luxembourg'),
    ('MO', u'Macao'),
    ('MK', u'Macedonia, The Former Yugoslav Republic of'),
    ('MG', u'Madagascar'),
    ('MW', u'Malawi'),
    ('MY', u'Malaysia'),
    ('MV', u'Maldives'),
    ('ML', u'Mali'),
    ('MT', u'Malta'),
    ('MH', u'Marshall Islands'),
    ('MQ', u'Martinique'),
    ('MR', u'Mauritania'),
    ('MU', u'Mauritius'),
    ('YT', u'Mayotte'),
    ('MX', u'Mexico'),
    ('FM', u'Micronesia, Federated States of'),
    ('MD', u'Moldova, Republic of'),
    ('MC', u'Monaco'),
    ('MN', u'Mongolia'),
    ('ME', u'Montenegro'),
    ('MS', u'Montserrat'),
    ('MA', u'Morocco'),
    ('MZ', u'Mozambique'),
    ('MM', u'Myanmar'),
    ('NA', u'Namibia'),
    ('NR', u'Nauru'),
    ('NP', u'Nepal'),
    ('NL', u'Netherlands'),
    ('NC', u'New Caledonia'),
    ('NZ', u'New Zealand'),
    ('NI', u'Nicaragua'),
    ('NE', u'Niger'),
    ('NG', u'Nigeria'),
    ('NU', u'Niue'),
    ('NF', u'Norfolk Island'),
    ('MP', u'Northern Mariana Islands'),
    ('NO', u'Norway'),
    ('OM', u'Oman'),
    ('PK', u'Pakistan'),
    ('PW', u'Palau'),
    ('PS', u'Palestinian Territory, Occupied'),
    ('PA', u'Panama'),
    ('PG', u'Papua New Guinea'),
    ('PY', u'Paraguay'),
    ('PE', u'Peru'),
    ('PH', u'Philippines'),
    ('PN', u'Pitcairn'),
    ('PL', u'Poland'),
    ('PT', u'Portugal'),
    ('PR', u'Puerto Rico'),
    ('QA', u'Qatar'),
    ('RE', u'R\xe9union'),
    ('RO', u'Romania'),
    ('RU', u'Russian Federation'),
    ('RW', u'Rwanda'),
    ('BL', u'Saint Barth\xe9lemy'),
    ('SH', u'Saint Helena, Ascension and Tristan Da Cunha'),
    ('KN', u'Saint Kitts and Nevis'),
    ('LC', u'Saint Lucia'),
    ('MF', u'Saint Martin (French Part)'),
    ('PM', u'Saint Pierre and Miquelon'),
    ('VC', u'Saint Vincent and the Grenadines'),
    ('WS', u'Samoa'),
    ('SM', u'San Marino'),
    ('ST', u'Sao Tome and Principe'),
    ('SA', u'Saudi Arabia'),
    ('SN', u'Senegal'),
    ('RS', u'Serbia'),
    ('SC', u'Seychelles'),
    ('SL', u'Sierra Leone'),
    ('SG', u'Singapore'),
    ('SX', u'Sint Maarten (Dutch Part)'),
    ('SK', u'Slovakia'),
    ('SI', u'Slovenia'),
    ('SB', u'Solomon Islands'),
    ('SO', u'Somalia'),
    ('ZA', u'South Africa'),
    ('GS', u'South Georgia and the South Sandwich Islands'),
    ('SS', u'South Sudan'),
    ('ES', u'Spain'),
    ('LK', u'Sri Lanka'),
    ('SD', u'Sudan'),
    ('SR', u'Suriname'),
    ('SJ', u'Svalbard and Jan Mayen'),
    ('SZ', u'Swaziland'),
    ('SE', u'Sweden'),
    ('CH', u'Switzerland'),
    ('SY', u'Syrian Arab Republic'),
    ('TW', u'Taiwan, Province of China'),
    ('TJ', u'Tajikistan'),
    ('TZ', u'Tanzania, United Republic of'),
    ('TH', u'Thailand'),
    ('TL', u'Timor-leste'),
    ('TG', u'Togo'),
    ('TK', u'Tokelau'),
    ('TO', u'Tonga'),
    ('TT', u'Trinidad and Tobago'),
    ('TN', u'Tunisia'),
    ('TR', u'Turkey'),
    ('TM', u'Turkmenistan'),
    ('TC', u'Turks and Caicos Islands'),
    ('TV', u'Tuvalu'),
    ('UG', u'Uganda'),
    ('UA', u'Ukraine'),
    ('AE', u'United Arab Emirates'),
    ('GB', u'United Kingdom'),
    ('US', u'United States'),
    ('UM', u'United States Minor Outlying Islands'),
    ('UY', u'Uruguay'),
    ('UZ', u'Uzbekistan'),
    ('VU', u'Vanuatu'),
    ('VE', u'Venezuela, Bolivarian Republic of'),
    ('VN', u'Viet Nam'),
    ('VG', u'Virgin Islands, British'),
    ('VI', u'Virgin Islands, U.S.'),
    ('WF', u'Wallis and Futuna'),
    ('EH', u'Western Sahara'),
    ('YE', u'Yemen'),
    ('ZM', u'Zambia'),
    ('ZW', u'Zimbabwe')
]
 



class CustomUser(AbstractUser,PermissionsMixin):
  
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and  false
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50, blank=True, null=True)
    username = models.CharField(_("user name"), unique=False, max_length=50, blank=True, null=True)
    phone_number = PhoneNumberField(_("phone number"), unique=True)
    phone_otp = models.CharField(max_length=6, blank=True, null=True)
    phone_otp_expiry = models.DateTimeField(_("phone otp expiry"), auto_now=False, auto_now_add=False, blank=True, null=True)
    phone_otp_resend = models.DateTimeField(_("phone otp resend"), auto_now=False, auto_now_add=False, blank=True, null=True)
    phone_otp_try = models.CharField(_("phone otp try"), max_length=2, default=0)
    phone_validated = models.BooleanField(default=False)
   
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    email_otp_expiry = models.DateTimeField(_("otp expiry"), auto_now=False, auto_now_add=False, blank=True, null=True)
    email_otp_resend = models.DateTimeField(_("email otp resend"), auto_now=False, auto_now_add=False, blank=True, null=True)
    email_otp_try = models.CharField(_("email otp try"),max_length=2, default=0)
    email_validated = models.BooleanField(default=False)

    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    profile_picture = models.ImageField(
        _('profile picture'), 
        upload_to="profile_images/",
        blank=True,
        null=True
    )
    
    bio = models.TextField(_('Bio'), max_length=500, null=True, blank=True)
    country = models.CharField(_("Country"),max_length=50, choices=countries_option)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name','phone_number','country']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    objects = CustomUserManager()

    @property
    def image_url(self):
        if self.profile_picture:
            return f"{settings.MEDIA_URL}{self.profile_picture}"
        return None

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        print("self user",self.country)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email
    